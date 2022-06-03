"""
DnD Dice Roller

Author: Eric Hargrove
Date Created: 6/1/21
Last Modified: 6/2/21
"""

import random
from colorama import Fore, Back, Style
import re

d4 = 4
d6 = 6
d8 = 8
d10 = 10
d12 = 12
d20 = 20

print("Attack dice? 4 = d4, 6 = d6, etc.")
atkDice = input()

print("What's your strength modifier?" + Style.RESET_ALL)
strMod = input()

print("What's your proficiency bonus?")
profBonus = input()

print("What's your initiative modifier?")
initMod = input()

print("Roll for initiative!")
initiative = random.randint(1, d20) + int(initMod)
print("Initiative = " + str(initiative))

def attack():
    roll = random.randint(1, int(atkDice))
    print("Damage roll = " + str(roll) + ", Attack Bonus = " + str(strMod))
    return 1 * roll + int(strMod)

def critFail():
    print(Fore.BLACK + Back.RED + "Crit Fail!" + Style.RESET_ALL)

prompt = ''

while(True):
    print("Want to attack? (y/n)")
    prompt = input()

    if (re.match("^[Yy]{1}$", prompt)):
        initRoll = random.randint(1, d20)
        print("d20 roll = " + str(initRoll))

        if (initRoll == 20):
            print(Fore.GREEN + "CRITICAL HIT!!!" + Style.RESET_ALL)
            critDamage = attack() * 2
            print("Damage Total = " + str(critDamage))
            continue

        if (initRoll == 1):
            critFail()
            continue

        def attackRoll():
            atkRoll = initRoll + int(strMod) + int(profBonus)
            print("Attack roll = " + str(atkRoll))

            print("Did it hit? (y/n)")
            hit = input()

            if(re.match("^[Yy]{1}$", hit)):
                print("Damage Total = " + str(attack()))

            elif (re.match("^[Nn]{1}$", hit)):
                print("You missed!")

            else:
                print("Invalid input")
                attackRoll()

        attackRoll()

    elif (re.match("^[Nn]{1}$", prompt)):
        print("Combat done")
        continue
    else:
        print("Invalid input")