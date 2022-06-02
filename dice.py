import random

d4 = 4
d6 = 6
d8 = 8
d10 = 10
d12 = 12
d20 = 20

print("Attack dice? 4 = d4, 6 = d6, etc.")
atkDice = input()

print("What's your strength modifier?")
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
    print("Crit Fail!")

prompt = ''

while(True):
    print("Want to attack? (y/n)")
    prompt = input()

    if(prompt == 'yes' or prompt == 'y'):
        initRoll = random.randint(1, d20)
        print("d20 roll = " + str(initRoll))

        if(initRoll == 20):
            print("CRITICAL!!!")
            critDamage = attack() * 2
            print("Damage Total = " + str(critDamage))
            continue

        if(initRoll == 1):
            critFail()
            continue

        atkRoll = initRoll + int(strMod) + int(profBonus)
        print("Attack roll = " + str(atkRoll))

        print("Did it hit? (y/n)")
        hit = input()

        if(hit == 'yes' or hit == 'y'):
            print("Damage Total = " + str(attack()))

        if (hit == 'no' or hit == 'n'):
            print("You missed!")

    if(prompt == 'no' or prompt == 'n'):
        print("Combat done")
        continue