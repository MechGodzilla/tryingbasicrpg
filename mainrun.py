import sys
import os
import random

from enemy import Goblin, Zombie
from player import Player

weapons = {"Great Sword": 40}

def main():
    os.system("cls")  # clear terminal
    print("Welcome to my game!\n"
          "1. Start\n"
          "2. Load\n"
          "3. Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        main()


def start():
    os.system("cls")
    print ("Hello, what is your name?")
    option = input("-> ")
    global playerIG
    playerIG = Player(option)
    start1()


def start1():
    print ("Hello %s, how are you? %s" % (playerIG.name, playerIG.name))
    print ("Name: %s" % playerIG.name)
    print ("Attack: %i" % playerIG.attack)
    print ("Gold: %d" % playerIG.gold)
    print ("Potions: %d" % playerIG.pots)
    print ("Health: %i/%i\n" % (playerIG.health, playerIG.maxhealth))
    print ("1.) Fight")
    print ("2.) Store")
    print ("3.) Save")
    print ("4.) Exit")
    option = input("-> ")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        pass
    elif option == "4":
        sys.exit()
    else:
        start1()
#
# goblin_ig = Goblin("Goblin")
# zombie_ig = Zombie("Zombie")

def prefight():
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = Goblin("Goblin")
    else:
        enemy = Zombie("Zombie")
    fight()


def fight():
    os.system("cls")
    print ("%s  vs  %s" %(playerIG.name, enemy.name))
    print ("%s's HP: %d / %d   %s's HP: %d / %d" % (playerIG.name, playerIG.health, playerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print ("1.) Attack")
    print ("2.) Drink Potion (%d)" % (playerIG.pots))
    print ("3.) Run")

    option = input("-> ")
    if option == "1":
        attack()
    elif option == "2":
        drinkpot()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    os.system("cls")
    player_attack = random.randrange(playerIG.attack//2, playerIG.attack) #lowest attack number, highest attack number
    enemy_attack = random.randrange(enemy.attack//2, enemy.attack)
    if player_attack == playerIG.attack//2:
        print("You miss!")
    else:
        enemy.health -= player_attack
        print("You did %s damage!" % player_attack)
    option = input(' ')
    # this isn't triggering??
    if enemy.health <= 0:
        win()
    os.system("cls")
    if enemy_attack == enemy.attack//2:
        print("%s attacks. You dodge!" % enemy.name)
    else:
        playerIG.health -= enemy_attack
        print("You take %i damage!" % enemy_attack )
    option = input(' ')
    if playerIG.health <= 0:
        dead()
    else:
        fight()

def drinkpot():
    os.system("cls")
    if playerIG.pots == 0:
        print("You do not have any potions!")
    else:
        playerIG.health += 50
        if playerIG.health > playerIG.maxhealth:
            playerIG.health = playerIG.maxhealth
        print("You drink a potion!")
    option = input(' ')
    fight()

def run():
    os.system("cls")
    runnum = random.randint(1,3)
    if runnum == 1:
        print("You ran away!")
        option = input(' ')
        os.system("cls")
        start1()
    else:
        print('You could not escape')
        option = input(' ')
        os.system('cls')
        enemy_attack = random.randrange(enemy.attack // 2, enemy.attack)
        if enemy_attack == enemy.attack // 2:
            print("%s attacks. You dodge!" % enemy.name)
        else:
            playerIG.health -= enemy_attack
            print("You take %i damage!" % enemy_attack)
        option = input(' ')
        if playerIG.health <= 0:
            dead()
        else:
            fight()

def store():
    pass

def win():
    os.system('cls')

    playerIG.gold += enemy.goldGain
    print('You defeated %s' % enemy.name)
    print('You found %i gold' % enemy.goldGain)
    option = input(' ')
    start1()

def dead():
    os.system('cls')
    print("You dead!")
    option = input(' ')
    sys.exit()

main()
