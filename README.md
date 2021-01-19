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

- Naviguer avec la carte dans rviz...

## Sans Map

- WebShell #2 : `roslaunch challenge challenge-1.2.launch`

- WebShell #3 : `rviz`

- Dans rviz : File -> Open Config -> Open "/home/user/catkin_ws/rviz/map.rviz"

- Naviguer sans la carte dans rviz...

# Challenge 2

- WebShell #1 : `roslaunch larm challenge-2.launch`

- WebShell #2 : `roslaunch challenge challenge-2.launch`

- WebShell #3 : `rviz`

- Dans rviz : File -> Open Config -> Open "/home/user/catkin_ws/rviz/map.rviz"

- Naviguer dans rviz pour trouver toutes les bouteilles

### Résultat attendu : La position approximative de la bouteille apparait dans le WebShell #2 :

```
[ BOTTLE ] Found at : 
...
```

# Challenge 3

WIP
