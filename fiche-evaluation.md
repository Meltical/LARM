# Évaluation intermédiaire

### Groupe évaluateur : groupe 14

Membres : (prénom nom)

 - > Vinciane Leclercq
 - > Enzo Bernard
 - > Erwan Merly

## Fiche d'identité du projet

- Groupe évalué : **groupe 15**
- Dépôt git : https://github.com/MikUwU/LARM
- numéro du commit (8 premiers caractères) : **8665ebe7**
- Date du commit : **Jan 13 22:33:14 2042**

cf. `git log`


## Grille d'évaluation générale

Chaque question est évaluée sur une échelle de -1 à 4:

- **-1** : Pire que rien, rien aurait été mieux, dans la mesure ou le peu présenté ne fait que témoigner de la non-compréhension du groupe par rapport à ce qui peut être attendu.
- **0** : Pas d'éléments, ou les éléments présents sont proche de rien (simple initialisation par exemple de ressources/fichiers pour l'instant vide).
- **1** : Ni fait Ni à faire, il y a des éléments qui vont dans le bon sens, mais trop peu ou erronés.
- **2** : Incomplet, les éléments répondent aux attentes dans l'ensemble, mais avec des lacunes sur certains points.
- **3** : Ok, les éléments répondent aux attentes. 
- **4** : Impecable, les éléments répondent aux attentes et vont au-delà du strict nécessaire.

En résumé : 

-1            |     0          |   1   |    2      |   3  |    4
--------------|----------------|-------|-----------|------|----------
Pire que rien | Pas d'éléments | Ni-ni | Incomplet |  Ok  | Impeccable

Notez que seules les notes **-1**, **0** et **3** ne requiére pas obligatoirement de commentaires.

## Installation

Concerne l'appropriation de la solution par les évaluateurs de façon à construire une solution prête à être évaluée et la documentation liée à cette action (notamment dans `README.md`).

1. La page d'accueil est propre et renseignée sur le projet ? 
   - Évaluation : **3**
   - Commentaire :
2. Les consignes d'installation sont faciles à trouver ?
   - Évaluation : **4**
   - Commentaire : Les commandes à entrer sont directement fournies
4. La procédure d'appropriation de la solution s'effectue sans encombre (clone/téléchargement ...) ?
   - Évaluation : **3**
   - Commentaire : Aucun soucis lors du clonage
5. La Construction de la solution s'effectue correctement (compilation ...) ?
   - Évaluation : **3**
   - Commentaire : Le catkin_make n'as posé aucun problème
6. Le protocole d'installation est clair et documenté ?
   - Évaluation : **4**
   - Commentaire : Toutes les commandes sont données et claires

## Challenge 1

Le robot se déplace dans un environnement encombré.

1. Le lancement du challenge s'effectue correctement (launch des `challenge-1.launch` et `navigation.launch`) ? 
   - Évaluation : **3**
   - Commentaire :
2. Les consignes quant aux opérations à effectuer par l'opérateur sont claires, cohérentes et minimales ?
   - Évaluation : **2**
   - Commentaire : "Naviguer avec RViz" trop large on ne parle pas des outils à utiliser
1. La réalisation des opérations s'effectue correctement ?
   - Évaluation : **3**
   - Commentaire : 1.2 fonctionne parfaitement, mais pas le 1.1 (le robot a du mal à se localiser seul dans la map)
2. Le robot se déplace correctement vers une position `goal` en évitant les obstacles ?
   - Evaluation : **3**
   - Commentaire :
3. Les trajectoires suivies par le robot sont souples et efficaces ?
   - Évaluation : **3**
   - Commentaire :
4. (BONUS) Le robot peut se déplacer en dehors de sa carte ou n'utilise pas de carte ?
   - Évaluation : **0**
   - Commentaire : ça ne fonctionne pas
5. Conclusion générale sur le challenge 1 ?
   - Évaluation : **3**
   - Commentaire : Globalement ça fontionne correctement !

## Challenge 2

Le robot cartographie et trouve les bouteilles dans un environnement de type intérieur/bureau.

1. Le lancement du challenge s'effectue correctement (sur la base des launchs appropriés) ? 
   - Évaluation : **3**
   - Commentaire :
2. Les consignes quant aux opérations à effectuer par l'opérateur sont claires, cohérentes et minimales ?
   - Évaluation : **2**
   - Commentaire : "Naviguer avec RViz" trop large on ne parle pas des outils à utiliser
3. La réalisation des opérations s'effectue correctement ?
   - Évaluation : **3**
   - Commentaire :
4. Le robot construit une carte au fil de ses déplacements ?
   - Évaluation : **3**
   - Commentaire :
5. Le robot est efficace pour détecter une bouteille lorsqu'elle est devant lui ? 
   - Évaluation : **3**
   - Commentaire : Il la détecte, et d'assez loin même
1. La position de la bouteille est remontée dans un topic approprié et visualisée dans `rviz` ?
   - Évaluation : **0**
   - Commentaire : Une position est renvoyée dans le webshell du launch. La position retrounée semble être celle du robot car elle change en permanence. Absence de topic /bottle
2. Le robot trouve toutes les bouteilles et sans faux positifs ?
   - Évaluation : **3**
   - Commentaire :
3. (BONUS) La position de chaque bouteille n'est envoyée qu'une seule fois (même si le robot repasse une seconde fois devant une bouteille déjà détectée) et l'affichage dans `rviz` est persistant ?
   - Évaluation : **0**
   - Commentaire : Renvoi continu de l'emplacement ed la bouteille et se redéclenche dès qu'on repasse devant
4.  Les sorties de la solution sont de bonne qualité (carte, position des objets dans la carte) ?
   - Évaluation : **2**
   - Commentaire : Carte propre, mais pas les positions qui sembles inexactes et renvoyées en continue
1. Conclusion générale sur le challenge 2 ?
   - Évaluation : **2**
   - Commentaire :  Lar partie cartographie et déplacement est ok, la reconnaissance se fait bien mais la signalisation et l'information envoyée sont inexactes

## Challendge 3

Le robot explore de façon autonomes un environnement de type intérieur/bureau.

1. Le lancement du challenge s'effectue correctement (sur la base des launchs appropriés) ? 
   - Évaluation : **0**
   - Commentaire :
2. Les opérations à effectuer par l'opérateur sont proches du néant ?
   - Évaluation : **0**
   - Commentaire :
3. Le robot se déplace efficacement de façon autonome ?
   - Évaluation : **0**
   - Commentaire :
4. La stratégie d'exploration (succession de position à atteindre) semble efficace ?
   - Évaluation : **0**
   - Commentaire :
5. Le robot détecte et communique la position des bouteilles quand il en croise une ?
   - Évaluation : **0**
   - Commentaire :
6.  Les sorties de la solution sont de bonne qualité (carte, position des abjects dans la carte) ?
   - Évaluation : **0**
   - Commentaire : 
5. (BONUS) Le robot s'arrête automatiquement lorsque sa carte est complète et le signale ?
   - Évaluation : **0**
   - Commentaire :
6. Conclusion générale sur le challenge 3 ?
   - Évaluation : **0**
   - Commentaire : Pas encore présent sur le dépot

## Le dépôt

On s'intéresse ici aux fichiers rendus via le dépôt en rentrant un peu plus dans les sources.
Attention, on évalue uniquement la branche principale, et le commit sus-mentionné.

1. Le dépôt est propre, les fichiers sont rangés dans les répertoires appropriés selon les préconisations ROS ? 
   - Évaluation : **3**
   - Commentaire :
2. Le dépôt est minimal, il ne contient que les fichiers sources utiles à la solution ? 
   - Évaluation : **3**
   - Commentaire :
3. Les launch files et les fichiers de paramètres sont bien nommés, clairs et concis ... ? 
   - Évaluation : **4**
   - Commentaire : Les launch file sont très bien commentés, clairs et rangés aux bons endroits
4. Les sources python ou Cpp sont propres (on peut ouvrir les sources et s'y retrouver) ?
   - Évaluation : **3**
   - Commentaire : La structure respect bien celle vue dans le cours et semble correcte (on aurait pu aimer quelques commentaires)
5. (si question précédente est à minima **2-incomplet**) les sources s'appuient sur des structures ou des classes et des fonctions unitaires quand il y a lieu de le faire ? 
   - Évaluation : **3**
   - Commentaire :
6. (si question précédente est à minima **2-incomplet**) les algorithmes mis en oeuvre 'semble' efficaces (pas de boucles inutiles, ou de possible optimisation évidente) ? 
   - Évaluation : **3**
   - Commentaire :

## Avis global sur la solution

Évaluation : **2** ( on devrait être ici sur **2-incomplet** )
Commentaire : Le challenge 1 est nickel, le 2 revoir l'affichage des positions et le 3 pas d'info (fait état des challenges qui peuvent être conservés validés et de ceux encore à faire et surtout fait la différence entre une solution ou ce qui est fait est propre et une solution ou tout ou partie de ce qui est fait est à revoir. Idéalement donc, seuls quelques points évalués **1** ou **2** l'ont été, car le travail est inachevé, autrement on rencontre essentiellement des **0** (point non encore adressé) **3** ou **4**.)
Avis : Tout devrait pouvoir être fait car il ne manque qu'une petite partie du travail pour l'affichages des positions et uniquement la partie déplacement autonome (est-ce qu'il vous semble compliqué pour le groupe évalué de finir le travail d'ici à vendredi ?)
Avis miroir : On devrait s'en sortir en ce qui concerne la navigation, cependant pour ce qui est de la vision, on a encore quelques points à voir *donc ça pourrait le faire* (est-ce qu'il vous semble compliqué pour vous (le groupe évaluateur) de finir le travail d'ici à vendredi ?)

