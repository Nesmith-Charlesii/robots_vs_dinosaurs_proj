from dinosaur_class import Dinosaur
from robot_class import Robot
from fleet_class import Fleet

if __name__ == '__main__':
    # instantiate 3 robots
    dex = Robot()
    robo_jojo = Robot()
    chappie = Robot()

    # instantiate 3 dinosaurs
    dino = Dinosaur()
    gino = Dinosaur()
    nino_brown = Dinosaur()

    # assign robot names
    dex.name = "dex"
    robo_jojo.name = "robo jojo"
    chappie.name = "chappie"

    # show robot stats
    dex.robot_stats()
    robo_jojo.robot_stats()
    chappie.robot_stats()

    # assign dinosaur type
    dino.type = 'raptor'
    gino.type = 'raptor'
    nino_brown.type = 'raptor'

    # show dinosaur stats
    dino.dinosaur_stats()
    gino.dinosaur_stats()
    nino_brown.dinosaur_stats()

    # instantiate a fleet and assign it a name
    fleet_1 = Fleet()
    fleet_1.fleet_name = 'New Jack City'

    # show fleet stats
    fleet_1.fleet_stats()

    # add robots to fleet
    fleet_1.add_to_fleet(dex)

    # show fleet stats
    fleet_1.fleet_stats()
