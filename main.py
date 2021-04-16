from robot_class import Robot
from dinosaur_class import Dinosaur

if __name__ == '__main__':
    dex = Robot()
    robo_jojo = Robot()
    chappie = Robot()

    dino = Dinosaur()
    gino = Dinosaur()
    nino_brown = Dinosaur()

    dex.name = "dex"
    robo_jojo.name = "robo jojo"
    chappie.name = "chappie"

    dex.robot_stats()
    robo_jojo.robot_stats()
    chappie.robot_stats()