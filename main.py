from classes.game import Person, bcolors, GameArt
from classes.magic import Spell
from classes.inventory import Item
import sys
import random

#Declaramos variables para almacenar los Players/Enemies que van perdiendo
defeated_enemies = 0
defeated_players = 0

art = GameArt()
art.print_title()

start_game = False

while not start_game:
    user_input = input(str("Do you want to start the game? y/n:"))
    if user_input == "y":
        start_game = True
    elif user_input == "n":
        sys.exit("You are a coward! Bye")
    else:
        print(user_input, "is not a valid option. Please write y or n")

art.print_fight_title()
art.print_dragon()

#   Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

#   Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

#   Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 1000 HP", 1000)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restors HP/MP of one parte member", 9999)
hielixir = Item("Mega-elixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Granade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiation of the Person Class. We create 3 players. We pass a list of objects to magic
player1 = Person("Alasmarath", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Faragoth", 4160, 65, 188, 311, player_spells, player_items)
player3 = Person("Geralt Of Rivia", 3089, 288, 60, 34, player_spells, player_items)
#   Instantiation of the enemies

enemy1 = Person("Imp", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Dragon", 11200, 500, 525, 25, enemy_spells, [])
enemy3 = Person("Imp", 1250, 130, 560, 325, enemy_spells, [])

#   We create a list of players
players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

start_battle = False

while not start_battle:
    user_input = input("Run (r) or attack (a):")
    if user_input == "a":
        start_battle = True
    elif user_input == "r":
        sys.exit("You are a coward! Bye")
    else:
        print(user_input, "is not a valid option. Please write y or n")

#   Battle Loop
while running:
    art.print_line()
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        correct_option = False

        while not correct_option:
            choice = input("\n    Choose action: ")
            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                correct_option = True
            else:
                print(choice, "is not a valid option. Please choose one of the numbers in the list")

        #   We reduce the input by 1
        # print("Your Choice was" + str(choice))
        index = int(choice) - 1
        # print("index is" + str(index))

        #   The player chose atk
        if index == 0:
            dmg = player.generate_damage()
            #   We return the index number of the enemy and save it
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("\n", bcolors.OKBLUE + bcolors.BOLD, " You attacked", enemies[enemy].name, "for", dmg,
                  "points of damage", bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                #   We delete the enemy from the list because it was defeated
                print(enemies[enemy].name + " has died.")
                defeated_enemies += 1
                del enemies[enemy]
        #   The player chose magic
        elif index == 1:
            #   We list the magic spells using choose_magic method
            player.choose_magic()

            correct_option = False

            while not correct_option:
                #   We capture user input and withdraw 1
                magic_choice = input("    Choose Magic: ")
                if magic_choice.isdigit():
                    magic_choice = int(magic_choice) - 1
                    if magic_choice == 0 or magic_choice == 1 or magic_choice == 2 or magic_choice == 3 or magic_choice == 4 or magic_choice == 5:
                        correct_option = True
                    else:
                        print(magic_choice + 1, "is not a valid option. Please choose one of the numbers in the list")
                else:
                    print(magic_choice, "is not a valid option. Please choose one of the numbers in the list")

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            #   We check the current MP
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
                continue

            #   We reduce the mp passing the cost variable as parameter
            player.reduce_mp(spell.cost)

            #   white magic heals
            if spell.type == "white":
                #   Here the magic_dmg is the amount of HP added to current HP.
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)

            elif spell.type == "black":
                #   We return the index number of the enemy and save it
                enemy = player.choose_target(enemies)
                #   Enemy takes magic damage
                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to "
                      + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    #   We delete the enemy from the list because it was defeated
                    print(enemies[enemy].name + " has died.")
                    defeated_enemies += 1
                    del enemies[enemy]

        #   The player chose item
        elif index == 2:
            player.choose_item()

            correct_option = False

            while not correct_option:
                item_choice = input("    Choose item: ")
                if item_choice.isdigit():
                    item_choice = int(item_choice) - 1
                    if item_choice == 0 or item_choice == 1 or item_choice == 2 or item_choice == 3 or item_choice == 4 or item_choice == 5:
                        correct_option = True
                    else:
                        print(item_choice + 1, "is not a valid option. Please choose one of the numbers in the list")
                else:
                    print(item_choice, "is not a valid option. Please choose one of the numbers in the list")

            item = player.items[item_choice]["item"]

            #   We check if the user has no more left
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "No " + item.name + " left..." + bcolors.ENDC)
                continue

            #   We reduce the item by 1
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

            elif item.type == "elixir":

                if item.name == "Mega-elixir":
                    #   We Heal all the players
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    #  Just a regular elixir
                    player.hp = player.maxhp
                    player.mp = player.maxmp

                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP." + bcolors.ENDC)

            elif item.type == "attack":
                #   We return the index number of the enemy and save it
                enemy = player.choose_target(enemies)
                #   Enemy takes item damage
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop),
                      "points of damage to " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    #   We delete the enemy from the list because it was defeated
                    print(enemies[enemy].name + " has died.")
                    defeated_enemies += 1
                    del enemies[enemy]
        #   The player chose to exit
        elif index == 3:
            sys.exit("You are a coward! Bye")

    #   We check if the battle is over

"""
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp == 0:
            defeated_players += 1
"""
    # We check if player won
    print("enemigos derrotados: ", defeated_enemies)
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    # We check if enemy won
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False

    print("\n")
    # Enemy attack phase
    art.print_line()
    print(bcolors.BOLD, "Enemy's turn", bcolors.ENDC)
    for enemy in enemies:
        #   Enemy chooses what to do
        enemy_choice = random.randrange(0, 2)

        #   We Check if the Enemy's HP is enough to cast the most expensive spell, if not it has to choose attack
        #   print("El MP del enemigo es:", enemy.get_mp())
        if enemy_choice == 1:
            if enemy.get_mp() < 50:
                print("Enemy has not enough MP so he decides to attack")
                enemy_choice = 0

        #   print("el length del array players es", len(players))
        players_list_length = len(players);

        #   Enemy chose to attack
        if enemy_choice == 0:
            #   We generate enemy damage and set a random target

            if players_list_length == 0:
                print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
                running = False
            else:
                target = random.randrange(0, players_list_length)
                enemy_dmg = enemy.generate_damage()
                #   We pass dmg to the player.take_damage
                #   print("el target es: " + str(target))
                players[target].take_damage(enemy_dmg)
                print("\n" + "    " + bcolors.FAIL, enemy.name, "attacks", players[target].name, "for", enemy_dmg,
                      bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name + " has died.")
                    defeated_players += 1
                    del players[target]

                # We check if enemy won
                if defeated_players == 2:
                    print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
                    running = False

        #   Enemy Chose Magic
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()

            # print("Enemy chose to use Magic! He used", spell.name, "damage is", magic_dmg)

            enemy.reduce_mp(spell.cost)

            #   print("Enemy MP is: " + str(enemy.get_mp()))

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.FAIL + spell.name + " heals", enemy.name, "for", str(magic_dmg), "HP" + bcolors.ENDC)

            elif spell.type == "black":

                if players_list_length == 0:
                    print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
                    running = False
                else:
                    target = random.randrange(0, players_list_length)

                    players[target].take_damage(magic_dmg)

                    print("\n" + "    " + bcolors.FAIL + enemy.name + "'s", spell.name + " spell deals", str(magic_dmg),
                          "points of damage to "
                          + players[target].name + bcolors.ENDC)

                    if players[target].get_hp() == 0:
                        print(players[target].name + " has died.")
                        defeated_players += 1
                        del players[target]

                        # We check if enemy won
                        if defeated_players == 2:
                            print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
                            running = False
