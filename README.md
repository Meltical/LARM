# PARTICIPANTS

Victor DELIEGE & Arthur VERGAERT - Gr 15

# Installation

- Créer un ROSJect Kinetic

- Dans WhebShell #1 :

```bash
rm -rf ~/catkin_ws
rm -rf ~/simulation_ws
git clone https://github.com/MikUwU/LARM.git ~/catkin_ws
git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git ~/simulation_ws
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
cd ~/simulation_ws/
catkin_make
source devel/setup.bash
```

- Dans WebShell #2 et #3 :

```bash
cd ~/catkin_ws/
source devel/setup.bash
cd ~/simulation_ws/
source devel/setup.bash
```

# Challenge 1

- WebShell #1 : `roslaunch larm challenge-1.launch`

## Avec Map

- WebShell #2 : `roslaunch challenge challenge-1.1.launch`

- WebShell #3 : `rviz`

- Dans rviz : File -> Open Config -> Open "/home/user/catkin_ws/rviz/map.rviz"

- Naviguer avec la carte dans rviz. Utiliser l'outil 2D Nav Goal.

## Sans Map

- WebShell #2 : `roslaunch challenge challenge-1.2.launch`

- WebShell #3 : `rviz`

- Dans rviz : File -> Open Config -> Open "/home/user/catkin_ws/rviz/map.rviz"

- Naviguer sans la carte dans rviz. Utiliser l'outil 2D Nav Goal.

# Challenge 2

- WebShell #1 : `roslaunch larm challenge-2.launch`

- WebShell #2 : `roslaunch challenge challenge-2.launch`

- WebShell #3 : `rviz`

- Dans rviz : File -> Open Config -> Open "/home/user/catkin_ws/rviz/map.rviz"

- Naviguer dans rviz pour trouver toutes les bouteilles. Utiliser l'outil 2D Nav Goal.

### Résultat attendu

La position approximative de la bouteille est publiée dans le topic /bottle. On peut le visualiser en ouvrant un nouveau WebShell avec : `rostopic echo /bottle`

# Challenge 3

- WebShell #1 : `roslaunch larm challenge-3.launch`

- WebShell #2 : `roslaunch challenge challenge-3.launch`

- WebShell #3 : `rviz`

- Dans rviz : File -> Open Config -> Open "/home/user/catkin_ws/rviz/map.rviz"

- Naviguer dans rviz pour trouver toutes les bouteilles. Utiliser l'outil "Publish Point" pour dessiner une zone dans laquelle le robot va explorer. Une fois la zone fermée, donner un dernier point à l'intérieur de celle-ci correspondant au point de départ au robot.

<center> <img src="https://raw.githubusercontent.com/MikUwU/LARM/main/frontier_exploration.gif" height="250" />
</center>

### Résultat attendu

La position approximative de la bouteille est publiée dans le topic /bottle. On peut le visualiser en ouvrant un nouveau WebShell avec : `rostopic echo /bottle`
