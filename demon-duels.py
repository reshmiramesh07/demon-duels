class Player:
    def __init__(self, name, weapon, won, total):
        self.name = name
        self.weapon = weapon
        self.won = won
        self.total = total

class Demon:
    def __init__(self, name, hp, basic, charged, spec, rate, defeat):
        self.name = name
        self.hp = hp
        self.basic = basic
        self.charged = charged
        self.spec = spec # spec for special move
        self.rate = rate # difficulty of duel
        self.defeat = defeat

# creating player object
player = Player("Player", "Sword", 0, 0)
weapons = ["Sword", "Dagger", "Javelin", "Bow and arrows", "Staff"]

# creating demon objects
poltergiest = Demon("Poltergiest", 50, "Throw", "Destroy", "Tornado", "Easy", 0) # destroy will destory player's weapon; player atk goes down 50%
all_demons = []

def poltergiest_basic():
    pass

def poltergiest_charged():
    pass

def poltergiest_spec():
    pass

def battle_poltergiest():
    pass

def player_setup():
    player.name = input("What is your name?: ")
    
def battle_select(): # or choose weapon here
    print("Pick your battle.")
    # pick battle print and input here
    print("Entering armory...")
    print("We have a lot to offer from our armory! As you gain more victories, more options will reveal themselves.")
    for i in range(len(weapons)):
        print("- " + weapons[i])
    player.weapon = input("Choose your weapon:") # babyproof this



player_setup()
