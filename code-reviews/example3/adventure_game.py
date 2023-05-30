# An interactive adventure game!
import random

def print_welcome():
    print("Welcome to the adventure game! 🛡")
    print("Maintain your health while finding food 🥕")
    print("But watch out for the wild animals! 🦊")
    print("And get the high score! 📈")
    print("")

def print_menu():
    print("1. Explore")
    print("2. Check status")
    print("3. Rest")
    print("4. Quit game")

def explore():
    global health
    global food
    global high_score
    global high_score_player_name
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
    score += 1
    if score > high_score:
        high_score = score
        high_score_player_name = player_name

def check_status():
     global health
     global food
     global score
     print("Health:", health)
     print("Food:", food)
     print("Score:", score)

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

def view_high_score():
    global high_score
    global high_score_player_name
    print("Highest score is: ", high_score)
    print("Acheived by player: ", high_score_player_name)

def quit_game():
    global game_on
    game_on = False
    print("Thanks for playing!")
    print("Final status:")
    check_status()

# Game Variables
game_on = True
health = 100
food = 10
score = 0
high_score = 0
high_score_player_name = ""
player_name = ""

while game_on:
    print_menu()
    player_name = input("What is your name?\n")
    choice = int(input("What would you like to do?\n"))
    if choice == 1:
        explore()
    elif choice == 2:
        check_status()
    elif choice == 3:
        rest()
    elif choice == 4:
        view_high_score()
    elif choice == 5:
        quit_game()
    else:
        print("Invalid choice, please select from the menu.")
