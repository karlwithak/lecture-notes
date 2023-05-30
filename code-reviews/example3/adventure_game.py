# An interactive adventure game!
import random

def print_welcome():
    print("Welcome to the adventure game! 🛡")
    print("Maintain your health while finding food 🥕")
    print("But watch out for the wild animals! 🦊")
    print("")

def print_menu():
    print("1. Explore")
    print("2. Check status")
    print("3. Rest")
    print("4. Quit game")

def explore():
    global health
    global food
    event = random.randint(1, 3)
    if event == 1:
        print("You found a berry bush! +5 food")
        food += 5
    elif event == 2:
        print("You were attacked by a wild animal! -5 health")
        health -= 5
    elif event == 3:
        print("You found a small creek! +10 health")
        health += 10
    else:
        print("You tripped and fell into a hole! -10 health")
        health -= 10
    if health > 100:
        health = 100
    elif health < 0:
        health = 0

def check_status():
     global health
     global food
     print("Health:", health)
     print("Food:", food)

def rest():
    global health
    global food
    if food > 0:
        print("You take a break and eat some food. +10 health, -5 food")
        health += 10
        food -= 5
    else:
        print("You have no food. You should explore and find some food.")
    if health > 100:
        health = 100

def quit_game():
    global game_on
    game_on = False
    print("Thanks for playing!")
    print("Final health: ", health)
    print("Final food: ", food)

# Game Variables
game_on = True
health = 100
food = 10

while game_on:
    print_menu()
    choice = int(input("What would you like to do? "))
    if choice == 1:
        explore()
    elif choice == 2:
        check_status()
    elif choice == 3:
        rest()
    elif choice == 4:
        quit_game()
    else:
        print("Invalid choice, please select from the menu.")
