# Applications Django de l'association JeBiF

L'association JeBiF met à jour ses applications Django. Dans ce document,
vous trouverez les différents modules réalisés et utilisés par l'assoiation dans
le cadre de son organisation interne et d'autres applications externes et publiques.

## BioInfuse

À l'occasion de la conférence [JOBIM 2016](http://jobim2016.sciencesconf.org/) qui aura
lieu à Lyon, JeBiF organise un concours de vidéo de vulgarisation scientifique.
Dans ce cadre, l'application BioInfuse permettra :

* de s'inscrire en tant que concurrent (role par défaut), jury ou administrateur
* pour les concurrents, de soumettre leur vidéo qui sera jugé par un jury sélectionné
spécifiquement pour ce concours
* pour les membres du jury, de juger les différentes vidéos proposés par les concurrents
* pour les administrateurs, différentes actions pour gérer les concours (création d'un nouveau
concours, gestion des membres inscrits, rédaction d'information sur les concours)

### Dépendances

* Dailymotion : `pip install dailymotion`
* urllib3, module connection : `pip install --upgrade urllib3`
* Markdown : `pip install markdown`

### Paramètrages

Pour utiliser cette application dans votre projet, vous devrez modifier les fichiers suivants :

* jebif/localsettings.py.dist : à copier dans jebif/localsettings.py et à modifier au niveau des paramètres attendus par Django (cf. Settings dans la documentation officielle pour plus de détails)
* bioinfuse/parameters.py : à copier dans bioinfuse/parameters.py et à modifier au niveau des paramètres attendus par Dailymotion