from django import get_version
from django.shortcuts import render, HttpResponseRedirect
from bioinfuse.models import *
#from django.db.models import Count
from bioinfuse.forms import *
from django.utils.timezone import now
from django.contrib.auth import authenticate, login


def base(request):
    context = {
        'version': get_version(),
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

def index(request):
    context = base(request)
    return render(request, "home.html", context)

def subscribe(request):
    registered = False
    context = base(request)
    if request.method == 'GET':
        user_form = NewUserForm()
        subs_form = SubscriptionForm()
    else:
        user_form = NewUserForm(request.POST)
        subs_form = SubscriptionForm(request.POST)

        if user_form.is_valid() and subs_form.is_valid():
            # register new user
            user = user_form.save()
            user.set_password(user.password) # use set_password to hash enter password
            user.save()
            show_name = subs_form.cleaned_data['show_name']
            # register new member
            member = subs_form.save(commit=False)
            member.user = user
            member.save()
            
            registered = True
            context['show_name'] = show_name

    context['user_form']  = user_form
    context['subs_form']  = subs_form
    context['registered'] = registered

    return render(request, "subscribe.html", context)

def connect(request):
    connected = False
    context = base(request)
    if request.method == 'GET':
        connect_form = ConnectForm()
    else:
        connect_form = ConnectForm(request.POST)

        if connect_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            context['username'] = username
            if user:
                if user.is_active:
                    login(request, user)
                    member = Member.objects.get(user=user)
                    connected = True
                    context['member'] = member
                else:
                    error_msg = "Compte inactif"
                    context['error_msg'] = error_msg
            else:
                error_msg = "Nom d'utilisateur inconnu"
                context['error_msg'] = error_msg

    context['connected'] = connected
    context['connect_form'] = connect_form
    
    return render(request, "connect.html", context)