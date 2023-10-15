## Description
Nous avions comme but de créer un objet en lien avec le domaine de la sécurité domotique. En effet, l'avancement de la technologie nous permet de créer des systèmes de sécurité plus avancer pour garder les gens et leurs domiciles en toute sûreté. Pour ce fait, nous avions décidé de créer un objet connecter qui détecte les intrusions et envoie une notification à l'utilisateur. Des objets similaires existent déjà sur le marché dont le Ring Doorbell qui, avec un détecteur de mouvement, commence à enregistre une vidéo.  De plus, lorsque quelqu’un sonne à la porte, la sonnette allume sa caméra pour envoyer une vidéo en temps réel des personnes qui sont devant leur domicile. Notre objet partage quelque similitude, comme un détecteur de mouvements, mais il comporte aussi un buzzer, une lumière led, un écran LCD et un bouton. Pour être plus précis notre objet à comme but de détecter les intrusions par le biais du mouvement. Quand un objet ou personne n’est détecté le buzzer sera déclenché et l’évènement sera enregistré dans une base de données dans lequel on retrouve la date précise de l’événement ainsi que l’utilisateur ayant ouvert la session. De ce fait une personne peut se créer un compte afin de démarrer des sessions. Une authentification est faite au démarrage de l’objet.

## Installation
Toutes les étapes suivantes se font à partir de votre raspberry pi.
Pour l’installation, il faut tout d’abord allez sur gitlab et téléchargez télécharger le répertoire principal. Par la suite, ouvrez un terminal et allez au répertoire principal (objetConnectéSecurité).  
Exécutez le script afin d’initier la base de données : sqlite3 alarm.db -init scriptBD.sql

Ensuite, assurez-vous d’avoir chacun des capteurs et effecteurs.  Veuillez-vous référer au WIKI  Schéma de branchement des capteurs et effecteurs  Pour l’installation.

Voici la liste complète des capteurs et effecteurs : 
IR obstacle Module, Active buzzer, Dual-color LED, Button, I2C LCD1602

## Utilisation
Pour utiliser l’objet vous devez exécuter le fichier python principal.py. Une fois dessus vous pouvez RUN le code. On vous recommence le IDE Thonny qui a été utilisé pour sa conception mais vous pouvez très bien utiliser d’autre IDE tel que PyCharm ou Visual studio Code. Une fois l’exécution est fait le programme roule automatiquement. 
## Protocole expérimental
Afin de vous assurer que l’objet est fonctionnel vous allez devoir faire quelques tests. Premièrement l’objet est neutre à son démarrage la lumière est (verte) au tout début. Quand cette lumière est allumée le module d’obstacles ne devrait pas déclencher le système d’alarme. Passez votre main en avant afin de vous assurer que c’est le cas. Une fois ce test effectué cliquez sur le bouton.  À ce moment votre lumière devrait passer au (rouge). La lumière rouge indique que le système est en alerte, veuillez mettre votre main devant le module d’obstacle. À ce moment le buzzer devrait être déclencher 3 fois de suite. Chaque fois qu’un obstacle est devant ce module il va déclencher le buzzer. Vous pouvez désactiver le système à nouveau avec le bouton. Celui-ci devrait être neutre et la lumière verte à nouveau.
## Vidéo
https://youtu.be/7wDj3NB9YwY
## À venir
L’ajout d’une caméra qui s’allume et commence à enregistrer lors d’une détection d’intrusion et envoie la vidéo enregistrée directement sur le cloud pour être stocké d’une manière sécurisée. Nous aimerons aussi rajouter un détecteur de son qui signale un son anormalement haut. 
## Contribution
Si vous souhaitez contribuer à notre projet sachez qu’il est Open source. Vous pouvez donc faire un Fork du projet et implémenter des fonctionnalités ou régler des bugs. Une fois que votre idée à été réalisé vous pouvez faire une requête de fusion. Cette requête va être en attente jusqu’à ce qu’elle soit analysée par l’un de nos programmeurs. Vous pouvez toujours vous fier à la section Documentation du répertoire principal pour vous aider dans la conception de votre objet. 
## Auteurs et remerciements
Notre Compagnie est composée de deux partenaires : Yassine Graitaa et Simon Bissonnette. Nous sommes très fiers d’avoir travaillé sur la réalisation de ce projet et nous avons très hâte d’en  développer d’autre . futur.

## Licence
Aucun droit d'auteur

La personne qui a associé une œuvre à cet acte a dédié l'œuvre au
domaine public en renonçant à tous ses droits sur l'œuvre dans le monde entier sous
le droit d'auteur, y compris tous les droits connexes et voisins,
dans la mesure permise par la loi.

Vous pouvez copier, modifier, distribuer et exécuter le travail, même à des fins commerciales
fins, le tout sans demander la permission. Voir Autres informations ci-dessous.

Les autres informations:

    * Les droits de brevet ou de marque de toute personne ne sont en aucun cas affectés
    par CC0, ni les droits que d'autres personnes peuvent avoir dans le travail ou dans
    la manière dont l'œuvre est utilisée, comme les droits à la publicité ou à la vie privée.

    * Sauf indication contraire expresse, la personne qui a associé une œuvre à
    cet acte ne donne aucune garantie sur le travail et décline toute responsabilité pour
    toutes les utilisations de l'œuvre, dans toute la mesure permise par la loi applicable.

    * Lorsque vous utilisez ou citez le travail, vous ne devez pas impliquer l'approbation
    par l'auteur ou l'affirmant.

## Statut du projet 
Cette version est encore une version bêta. Nous sommons présentement en train de développer des améliorations dont un système d’authentification à 2 facteurs (2FA) et sur l’expansion de notre entreprise à travers le monde.


