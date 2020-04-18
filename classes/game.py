import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class GameArt:

    def __init__(self):
        self.dragon = """
    
                                         ==(W{==========-      /===-                        
                                          ||  (.--.)         /===-_---~~~~~~~~~------____  
                                          | \_,|**|,__      |===-~___                _,-' `
                             -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~      
                         ______-==|        /`\_. .__/\ \    | |  \\           _-~`         
                   __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'             
                _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /               
              .'        /       |   \\      /~\___/~~\/  /' /        \   /'                
             /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                  
            /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   
                              \_|      /        _) | ;  ),   __--~~                        
                                '~~--_/      _-~/- |/ \   '-~ \                            
                               {\__--_/}    / \\_>-|)<__\      \                           
                               /'   (_/  _-~  | |__>--<__|      |                          
                              |   _/) )-~     | |__>--<__|      |                          
                              / /~ ,_/       / /__>---<__/      |                          
                             o-o _//        /-~_>---<__-~      /                           
                             (^(~          /~_>---<__-      _-~                            
                            ,/|           /__>--<__/     _-~                               
                         ,//('(          |__>--<__|     /                  .----_          
                        ( ( '))          |__>--<__|    |                 /' _---_~\        
                     `-)) )) (           |__>--<__|    |               /'  /     ~\`\      
                    ,/,'//( (             \__>--<__\    \            /'  //        ||      
                  ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       
                `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  
              ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    
               ;'( ')/ ,)(                              ~~~~~~~~~~                         
              ' ') '( (/                                                                   
                '   '  `                            
            """
        self.title = """
        
                               (                               (                             
              *   )   )        )\ )                            )\ ) (                        
            ` )  /(( /(   (   (()/(  (      ) (  (            (()/( )\   ) (      (  (       
             ( )(_))\()) ))\   /(_)) )(  ( /( )\))( (   (      /(_)|(_| /( )\ )  ))\ )(  (   
            (_(_()|(_)\ /((_) (_))_ (()\ )(_)|(_))\ )\  )\ )  (_))  _ )(_)|()/( /((_|()\ )\  
            |_   _| |(_|_))    |   \ ((_|(_)_ (()(_|(_)_(_/(  / __|| ((_)_ )(_)|_))  ((_|(_) 
              | | | ' \/ -_)   | |) | '_/ _` / _` / _ \ ' \)) \__ \| / _` | || / -_)| '_(_-< 
              |_| |_||_\___|   |___/|_| \__,_\__, \___/_||_|  |___/|_\__,_|\_, \___||_| /__/ 
                                             |___/                         |__/              
        """
        self.fight_title = """
                                                                          
  *   )   )        (                )    )     (                          
` )  /(( /(   (    )\ ) (  (  (  ( /( ( /(   ( )\    (  (  ( (            
 ( )(_))\()) ))\  (()/( )\ )\))( )\()))\())  )((_)  ))\ )\))()\  (    (   
(_(_()|(_)\ /((_)  /(_)|(_|(_))\((_)\(_))/  ((_)_  /((_|(_))((_) )\ ) )\  
|_   _| |(_|_))   (_) _|(_)(()(_) |(_) |_    | _ )(_))  (()(_|_)_(_/(((_) 
  | | | ' \/ -_)   |  _|| / _` || ' \|  _|   | _ \/ -_)/ _` || | ' \)|_-< 
  |_| |_||_\___|   |_|  |_\__, ||_||_|\__|   |___/\___|\__, ||_|_||_|/__/ 
                          |___/                        |___/              
"""

    def print_dragon(self):
        print(self.dragon)

    def print_title(self):
        print(self.title)

    def print_fight_title(self):
        print(self.fight_title)


class Person:
    #   STATS OF THE PLAYER
    def __init__(self, name, hp, mp, atk, df, magic, items):
        #   we set a maximum hp points
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        #   attack low
        self.atkl = atk - 10
        #   attack high
        self.atkh = atk + 10
        self.df = df
        # List of objects of instantiated Spells
        self.magic = magic
        # List of items
        self.items = items
        self.actions = ["Attack", "Magic", "Items", "Exit Game"]
        self.name = name

    def generate_damage(self):
        #   Dynamic amount of damage
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    #   In this case dmg is the amount of healing points added to HP
    def heal(self, dmg):
        # current HP + amount of healing points of the spell
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":", item["item"].description,
                  " (x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp != 0:
                print("        " + str(i) + "." + enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice

    def get_enemy_stats(self):
        print("\n")
        # Add spaces to name
        name_length = len(self.name)
        n_spaces = 26 - name_length
        spaces = ''
        i = 0
        while i < n_spaces:
            spaces += " "
            i = i + 1

        hp_bar = ""
        bar_ticks = self.hp / self.maxhp * 100 / 2

        while bar_ticks > 0:
            hp_bar += "/"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        #   We check againt the longest the string can be, which is 11
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                           HP " + current_hp)
        print("                            __________________________________________________")
        print(bcolors.BOLD + bcolors.FAIL + self.name + ":" + spaces + bcolors.ENDC + "|" + bcolors.BOLD +
              bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        print("\n")

        # Add spaces to name
        name_length = len(self.name)
        n_spaces = 26 - name_length
        spaces = ''
        i = 0
        while i < n_spaces:
            spaces += " "
            i = i + 1

        # Calculate the progress bar
        hp_bar = ""
        #   We divide by 4 because the HP bar has 25 characters which is 1/4 of 100
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while mp_ticks > 0:
            mp_bar += "/"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        while bar_ticks > 0:
            #   We add a "/" until we run out of bar_ticks
            hp_bar += "/"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            #   We add spaces until we complete the bar with 25 chars (ticks + spaces)
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        #   We check against the longest the string can be, which is 9
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        #   7 is max assuming that we have 6 numbers and the "/"
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                           HP " + current_hp + "                         MP " + current_mp)
        print("                            _________________________           __________")
        print(bcolors.BOLD + self.name + ":" + spaces + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC +
              bcolors.BOLD + "|         |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        #   if the magic points are less than the spell's cost or the spell type is white and life is grater than
        #   fifty per cent
        if self.mp < spell.cost or (spell.type == "white" and pct > 50):
            # print("el costo del spell es:", str(spell.cost))
            # print("el MP del NPC es:", str(self.mp))
            return self.choose_enemy_spell()
        else:
            return spell, magic_dmg
