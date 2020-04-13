from classes.game import Person, bcolors

#   Magic List
magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

# Instantiation of the Person Class
player = Person(460, 65, 60, 34, magic)
#   Instantiation of the enemy
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

#   Battle Loop
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
        print("You attacked for", dmg, "points of damage")
    elif index == 1:
        #   We list the magic spells using choose_magic method
        player.choose_magic()
        #   We capture user input and withdraw 1
        magic_choice = int(input("Choose Magic:")) - 1
        #   We randomly generate spell damage between mgl and mgh
        magic_dmg = player.generate_spell_damage(magic_choice)
        #   We assign spell name to a variable
        spell = player.get_spell_name(magic_choice)
        #   We assign the mp cost of the spell to a variable
        cost = player.get_spell_mp_cost(magic_choice)

        #   We check the current MP
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
            continue

        #   We reduce the mp passing the cost variable as parameter
        player.reduce_mp(cost)

        #   Enemy takes magic damage
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    #   Enemy attacks
    enemy_choice = 1

    #   We generate enemy damage
    enemy_dmg = enemy.generate_damage()

    #   We pass dmg to the player.take_damage
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("===========================================================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)



    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
