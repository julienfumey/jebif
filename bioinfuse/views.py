from django import get_version
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from bioinfuse.models import *
from bioinfuse.forms import *
import dailymotion
import pp
# from django.utils.timezone import now

def base(request):
    total_member = Member.objects.count()
    total_challenger = Member.objects.filter(role='C').count()
    total_jury = Member.objects.filter(role='J').count()
    total_admin = Member.objects.filter(role='A').count()
    context = {
        'version': get_version(),
        'total_member': total_member,
        'total_challenger': total_challenger,
        'total_jury': total_jury,
        'total_admin': total_admin,
    }
    if request.user.id:
        member_id = request.user.id
        context['member'] = Member.objects.get(user=member_id)
    challenge = Challenge.objects.filter(is_open=True).order_by('stop_date')
    if challenge:
        context['challenge'] = challenge[0]
    else:
        context['challenge.is_open'] = False
    return context


# Fix login redirection problem
def home(request):
    return HttpResponseRedirect(reverse('bioinfuse:index'))


def index(request):
    context = base(request)
    return render(request, "home.html", context)


def subscribe(request):
    registered = False
    context = base(request)
    challenge = Challenge.objects.filter(is_open=True).order_by('stop_date')[0]
    if request.method == 'GET':
        user_form = NewUserForm()
        subs_form = SubscriptionForm()
    else:
        user_form = NewUserForm(request.POST)
        subs_form = SubscriptionForm(request.POST)

        if user_form.is_valid() and subs_form.is_valid():
            # register new user
            user = user_form.save()
            user.set_password(user.password)  # use set_password to hash enter password
            user_member = user.id
            user.save()
            show_name = subs_form.cleaned_data['show_name']
            # register new member
            member = subs_form.save(commit=False)
            member.user = user
            member.save()
            # generate associated key for new member
            import random
            key = "".join([random.choice("abcdefghijklmnopqrstuvwxyz012"
                                         "3456789!@#$%^&*(-_=+)")
                           for i in range(50)])
            member_key = AssociatedKey.objects.create(candidate=member,
                                                      challenge=challenge,
                                                      associated_key=key)
            member_key.save()
            member = Member.objects.get(user=user_member)
            member.associated_key = member_key.associated_key
            member.save()
            registered = True
            context['show_name'] = show_name

    context['user_form'] = user_form
    context['subs_form'] = subs_form
    context['registered'] = registered

    return render(request, "subscribe.html", context)


def login(request):
    context = base(request)
    if request.method == 'GET':
        user_form = LoginUserForm()
    else:
        user_form = LoginUserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('bioinfuse:index'))
                else:
                    context['error_msg'] = "Le compte n'est pas actif."
            else:
                context['error_msg'] = "Le compte n'existe pas."

    context['user_form'] = user_form

    return render(request, "registration/login.html", context)


def edit_profile(request, member):
    context = base(request)
    get_member = Member.objects.get(user=member)
    get_user = User.objects.get(id=member)
    if request.method == 'GET':
        user_form = EditUserForm({'first_name': get_user.first_name,
                             'last_name': get_user.last_name,
                             'email': get_user.email})
        member_form = EditProfileForm({'show_name': get_member.show_name})
    else:
        user_form = EditUserForm(request.POST)
        member_form = EditProfileForm(request.POST)

        if user_form.is_valid() and member_form.is_valid():
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            show_name = member_form.cleaned_data['show_name']
            # update page
            get_user.first_name = first_name
            get_user.last_name = last_name
            get_user.email = email
            get_user.save()
            get_member.show_name = show_name
            get_member.save()
            return HttpResponseRedirect(reverse('bioinfuse:index'))
    context['profile_id'] = get_member.user.id
    context['user_form'] = user_form
    context['member_form'] = member_form
    return render(request, "edit_profile.html", context)


def list_members(request):
    context = base(request)
    members = Member.objects.all()
    if request.user.id:
        role = Member.objects.get(user=request.user.id).role
    else:
        role = 'I'
    context['members'] = members
    context['role'] = role
    return render(request, "manage_members.html", context)


def edit_member(request, member):
    context = base(request)
    get_member = Member.objects.get(user=member)
    changed_member = get_member
    get_user = User.objects.get(id=member)
    if request.user.id:
        role = Member.objects.get(user=request.user.id).role
    else:
        role = 'I'
    if request.method == 'GET':
        user_form = ManageUserForm({'first_name': get_user.first_name,
                                  'last_name': get_user.last_name,
                                  'email': get_user.email})
        member_form = ManageMemberForm({'show_name': get_member.show_name,
                                       'role': get_member.role})
    else:
        user_form = ManageUserForm(request.POST)
        member_form = ManageMemberForm(request.POST)

        if user_form.is_valid() and member_form.is_valid():
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            show_name = member_form.cleaned_data['show_name']
            member_role = member_form.cleaned_data['role']
            # update page
            get_user.first_name = first_name
            get_user.last_name = last_name
            get_user.email = email
            get_user.save()
            get_member.show_name = show_name
            get_member.role = member_role
            get_member.save()
            return HttpResponseRedirect(reverse('bioinfuse:manage_members'))
    context['role'] = role
    context['changed_member'] = changed_member
    context['user_form'] = user_form
    context['member_form'] = member_form
    return render(request, "edit_member.html", context)


def submit_movie(request, member):
    def submit_movie(d, file, data):
        url = d.upload(file)
        movie = d.post('/me/videos',
                       {'url': url, 'title': data['title'],
                        'published': 'true', 'channel': 'tech',
                        'private': 'true',
                        'description': data['description']})
        return movie
    context = base(request)
    role = Member.objects.get(user=member).role
    if request.method == 'GET':
        submit_movie_form = SubmitMovieForm({'submit_date': now()})
    else:
        submit_movie_form = SubmitMovieForm(request.POST)

    context['submit_movie_form'] = submit_movie_form
    context['role'] = role
    return render(request, "submit_movie.html", context)