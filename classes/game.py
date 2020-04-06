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


class Person:
    #   STATS OF THE PLAYER
    def __init__(self, hp, mp, atk, df, magic):
        #   we set a maximum hp points
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        # Dictionary of different magic spells
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        #   Dynamic amount of damage
        return random.randrange(self.atkl, self.atkh)

    
