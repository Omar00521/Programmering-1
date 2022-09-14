


import random

for _ in range(11):

    computer = random.choice(["rock", "paper", "scissors"])

    user = input("rock, paper or scissors? ")

    print("The computer chose", computer,"and the user chose", user +".")

    if computer == ("rock") and user == ("paper"):
        print("user wins") 

    if computer == ("rock") and user == ("scissors"): 
        print("Computer wins")

    if computer == ("rock") and user == ("rock"):
        print ("it's a draw -_-")

    if computer == ("paper") and user == ("scissors"):
         print ("user wins")

    if computer == ("rock") and user == ("scissors"):
        print ("computer wins!")

    if computer == ("scissors") and user == ("paper"):
            print ("computer wins")

    if computer == ("paper") and user == ("paper"):
        print ("Draw Loser")

    if computer == ("paper") and user == ("rock"):
        print ("Npc Wins!")

    if computer == ("scissors") and user == ("rock"):
        print ("You win!")
    
    if computer == ("scissors") and user == ("scissors"):
        print ("It's a draw buddy")