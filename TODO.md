# À faire

## Inscription

* [ ]Inscription d'un nouvel utilisateur :
    * [x] Utilise la table User de Django
    * [x]Étend la table avec les champs :
        * [x] show_name : le nom affiché sur BioInfuse
        * [x] role : le rôle de l'utilisateur  (concurrent, jury, admin)
        * [ ] associated_key : la clé unique associée à  l'utilisateur pour le concours
* [x] Page de connection
* [x] Page de deconnection
* [ ] Ajouter automatiquement une nouvelle clé d'association pour l'utilisateur
* [ ] Associer la clé au concours

## Clé d'association

La clé d'association ne peut pas être créée si aucun concours n'est ouvert.

À l'ouverture d'un nouveau concours, regénérer des clés d'association pour
les utilisateurs existants qui sont dans la table bioinfuse et qui sont actifs.

## Utilisateurs

* [x] Page de modification de profil pour l'utilisateur (champ role non utilisé)
* [ ] Page de modification de role pour un utilisateur pour les administrateurs
définis dans la table bioinfuse
* [ ] Page de soumission de vidéo pour l'utilisateur Concurrent
* [ ] Page des vidéos soumises pour l'utilisateur Jury
* [ ] Page d'évalution d'une vidéo pour l'utilisateur Jury

## Soumission d'une vidéo

* [ ] Basé sur l'API de DailyMotion en précisant le compte de JeBiF