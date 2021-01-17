# Breizhibus
Ce projet contient un fichier Notebook contenant le code pour une interface console, et un fichier python contenant la première partie du code demandé afin de réaliser une interface graphique sous Tkinter. De plus, un fichier SQL de notre base de données Breizhibus est aussi présent.


## Base de Données
Le projet initial proposait un programme demandant d'effectuer différentes requêtes vers notre base de données conçue à cet effet. La base contient une table contenant la liste des Lignes, des arrêts, des bus, et une table intermédiaire reliant les Lignes à leurs adresses. La conception de la base est présentée ci-dessous :
![designer_bdd.png](../images/designer_bdd.png)


## Console
Dans un premier temps, un affichage console suffisait pour répondre aux différentes problématiques :
	*Afficher les lignes, et leurs adresses respectives. Un affichage des bus empruntant ces lignes a aussi été ajouté.
	*Un programme permettant de gérer les bus (En insérer de nouveaux, en supprimer, en modifier).
	*Un programme calculant l’itinéraire le plus rapide pour atteindre un arrêt de bus particulier (cette dernière étape n’a pas été réalisée).
Le programme console sur Jupyter Notebook comprend une fonction générale de Menu permettant d’accéder aux autres fonctions. Une fois une fonction réaliser, le menu est accessible automatiquement.  

Afin d’accéder aux différentes informations, une connexion à la base de données a été établie et nos requêtes spécifiques ont été réalisées. De nombreux  `input` ont été placées afin de donner une certaine interactivité à notre application.
Le programme contient 5 fonctions :
	Une fonction `intro_app` contenant les requêtes d’affichage  des lignes, de leurs arrêts et de leurs bus correspondants.
	Une fonction `insert_bus` permettant d’ajouter de nouveaux bus à une ligne spécifique déclarée en amont.
	Une fonction `del_bus` supprimant un bus en déclarant son numéro dans une entrée `input` .
	Une fonction `update_bus` modifiant le numéro et/ou l’immatriculation d’un bus.
	Enfin, une fonction `menu_bus` reliant les autres fonctions de notre application et de pouvoir le fermer.
  

## Les points à améliorer
Outre le fait qu’il ne soit pas très « UX friendly » en affichant le programme dans la console, le programme comporte certains défauts, notamment dans les possibilités d’entrées de valeurs dans les `input` (On ne peut répondre par exemple que par O et N majuscule).
Plusieurs soucis d’entrées pourraient être anticipés, notamment dans les fonctions de gestion de bus. En effet, il manque certaines restrictions au niveau de la taille de caractères utilisés, de leur type. Les différentes données spécifiques à un bus peuvent être assignées à un autre etc… 
De nombreuses restrictions qui  incitent à réaliser une interface graphique.


## Interface Graphique
Le fichier python permet d’exécuter l’application à travers une interface graphique réalisée sous Tkinter.  Cette interface contient seulement la première fonction Affichage des Lignes et de leurs adresses correspondantes. 
Afin de préparer d’éventuels ajouts (Gestion des bus entre autre), un menu déroulant utilisant la méthode `.OptionMenu`  a été créé. En cliquant sur la première option « Affichage des lignes », une requête SQL est activée, affichant des boutons dans une Frame prévue à cet effet. Ces boutons générés par une boucle `For` ont le nom de la ligne correspondante et une couleur spécifique venant d’une liste.
En cliquant sur l’un de ces boutons, leurs adresses d’arrêt s’affichent dans un label. Un Widget Destroy est réalisé sur la Frame contenant le Label des adresses en cliquant sur un autre bouton, afin d’éviter l’accumulation des précédents Labels générés par les autres boutons.


## Difficultés
Pas de difficulté particulière au niveau des requêtes. Les problèmes ont surtout été rencontrés sur l’interface Tkinter, notamment au niveau du Callback.
