import random

print("Welcome to die")

def diceRoll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sum = die1 + die2
    print("Die 1: %d, Die 2: %d, You move: %d spaces" % (die1, die2, sum))
    if die1 == die2:
        print("Doubles")
        diceRoll()
    else:
        print("Next Player's Turn")

diceRoll()
