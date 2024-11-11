class Player:
    def __init__(self, name, weapon, won, total):
        self.name = name
        self.weapon = weapon
        self.won = won
        self.total = total

player = Player("Player", "Sword", 0, 0)
weapons = ["Sword", "Dagger", "Javelin", "Bow and arrows", "Staff"]

def player_setup():
    player.name = input("What is your name?: ")
    print("We have a lot to offer from our armory! As you gain more victories, more options will reveal themselves.")
    # for loop print each weapon

# functions - change_weapon, change_armor?

player_setup()
