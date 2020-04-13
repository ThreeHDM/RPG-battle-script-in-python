from classes.game import Person, bcolors
from classes.magic import Spell

#   Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

#   Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Instantiation of the Person Class. We pass a list of objects to magic
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
#   Instantiation of the enemy
enemy = Person(1200, 65, 45, 25, [])

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

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        #   We check the current MP
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
            continue

        #   We reduce the mp passing the cost variable as parameter
        player.reduce_mp(spell.cost)

        #   Enemy takes magic damage
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

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
