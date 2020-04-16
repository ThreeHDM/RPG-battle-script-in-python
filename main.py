from classes.game import Person, bcolors, GameArt
from classes.magic import Spell
from classes.inventory import Item
import sys

art = GameArt()
art.print_title()

start_game = True

while not start_game:
    user_input = input(str("Do you want to start the game? y/n:"))
    if user_input == "y":
        start_game = True
    else:
        sys.exit("You are a coward! Bye")

art.print_fight_title()
art.print_dragon()


#   Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

#   Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#   Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restors HP/MP of one parte member", 9999)
hielixer = Item("Mega-elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Granade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiation of the Person Class. We create 3 players. We pass a list of objects to magic
player1 = Person("Alasmarath", 3260, 65, 60, 34, player_spells, player_items)
player2 = Person("Faragoth", 4160, 65, 60, 34, player_spells, player_items)
player3 = Person("Geralt Of Rivia", 3089, 65, 60, 34, player_spells, player_items)
enemy = Person("Dragon", 1200, 65, 45, 25, [], [])

#   We create a list of players
players = [player1, player2, player3]


#   Instantiation of the enemy


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

#   Battle Loop
while running:
    print("===========================================================")
    for player in players:
        player.get_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action:")
        #   We reduce the input by 1
        index = int(choice) - 1

        #   The player chose atk
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage")
        #   The player chose magic
        elif index == 1:
            #   We list the magic spells using choose_magic method
            player.choose_magic()
            #   We capture user input and withdraw 1
            magic_choice = int(input("    Choose Magic:")) - 1

            if magic_choice == -1:
                continue

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
                #   Enemy takes magic damage
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        #   The player chose item
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

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
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP." + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)
        elif index == 3:
            sys.exit("You are a coward! Bye")

    #   Enemy attacks
    enemy_choice = 1

    #   We generate enemy damage
    enemy_dmg = enemy.generate_damage()

    #   We pass dmg to the player.take_damage
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("===========================================================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    """
    print("Your HP:", bcolors.OKGREEN + str(player1.get_hp()) + "/" + str(player1.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player1.get_mp()) + "/" + str(player1.get_max_mp()) + bcolors.ENDC)
    """

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
