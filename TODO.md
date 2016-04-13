# À faire

## Inscription

* Inscription d'un nouvel utilisateur :
    * Utilise la table User de Django 
    * Étend la table avec les champs :
        * show_name : le nom affiché sur BioInfuse
        * role : le rôle de l'utilisateur  (concurrent, jury, admin)
        * associated_key : la clé unique associée à  l'utilisateur pour le concours
* Page de connection
* Page de deconnection 
* Ajouter automatiquement une nouvelle clé d'association pour l'utilisateur
* Associer la clé au concours

## Clé d'association

La clé d'association ne peut pas être créée si aucun concours n'est ouvert.

À l'ouverture d'un nouveau concours, regénérer des clés d'association pour
les utilisateurs existants qui sont dans la table bioinfuse et qui sont actifs.

## Utilisateurs

* Page de modification de profil pour l'utilisateur (champ role non utilisé)
* Page de modification de role pour un utilisateur pour les administrateurs définis dans la table bioinfuse
