from dinosaur_class import Dinosaur
from robot_class import Robot
from fleet_class import Fleet
from herd_class import Herd
from weapon_class import Weapon
from battlefield_class import Battlefield

if __name__ == '__main__':

    # battlefield = Battlefield
    # battlefield.run_game()

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
    print(dex.robot_stats())
    print(robo_jojo.robot_stats())
    print(chappie.robot_stats())

    # assign dinosaur type
    dino.type = 'raptor'
    gino.type = 't-rex'
    nino_brown.type = 'triceratops'

    # show dinosaur stats
    dino.dinosaur_stats()
    gino.dinosaur_stats()
    nino_brown.dinosaur_stats()

    # instantiate a fleet and assign it a name
    fleet_1 = Fleet()
    fleet_1.fleet_name = 'New Jacks'

    # show fleet stats
    fleet_1.fleet_stats()

    # add robots to fleet
    print(fleet_1.add_to_fleet(dex))
    print(fleet_1.add_to_fleet(robo_jojo))
    print(fleet_1.add_to_fleet(chappie))

    # show fleet stats
    fleet_1.fleet_stats()

    # instantiate a herd
    herd_1 = Herd()

    # assign the herd a name
    herd_1.herd_name = "land before time"

    # add dinosaurs to herd --> for multiple, separate with commas
    print(herd_1.add_to_herd(dino, gino, nino_brown))

    # show herd stats
    herd_1.herd_stats()

    # Instantiate a weapon object. Display weapon. Generate a weapon
    weapon_1 = Weapon()
    weapon_1.display_weapon()
    print(weapon_1.generate_weapon())

    # display weapon and attain weapon
    weapon_1.display_weapon()
    print(dex.attain_weapon(weapon_1))

    # display robot full stats
    dex.robot_stats()

    # attack dinosaur
    print(dex.attack(nino_brown))
    print(dex.attack(nino_brown))
    print(dex.attack(nino_brown))
    print(dex.attack(nino_brown))

    # attack robot
    print(gino.attack(dex))
    print(gino.attack(dex))
    print(gino.attack(dex))
    print(gino.attack(dex))

    fleet_1.fleet_stats()


