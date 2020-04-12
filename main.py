from classes.game import Person, bcolors

#   Magic List
magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

# Instantiation of the Person Class
player = Person(460, 65, 60, 34, magic)
#   Instantiation of the enemy
enemy = Person(1200, 65, 45, 25, magic)


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("===========================================")
    player.choose_action()
    choice = input("Choose action:")
    #   We reduce the input by 1
    index = int(choice) - 1

    #   The player chose atk
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    #   Enemy attacks
    enemy_choice = 1

    #   We generate enemy damage
    enemy_dmg = enemy.generate_damage()

    #   We pass dmg to the player.take_damage
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())