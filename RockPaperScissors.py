import random

def ifState():
    computerGen = ['Rock', 'Paper', 'Scissors']

    computerChoice = random.choice(computerGen)

    userInput = input("Please select your weapon of choice \n")

    if userInput == "Rock":
        print('You have selected Rock and computer chose ' + computerChoice)
        if computerChoice == "Paper":
            print("YOU LOSE")
        elif computerChoice == "Scissors":
            print("YOU WIN")
        elif computerChoice == "Rock":
            print("TIE")
    elif userInput == "Paper":
        print('You have selected Paper and computer chose ' + computerChoice)
        if computerChoice == "Scissors":
            print("YOU LOSE")
        elif computerChoice == "Rock":
            print("YOU WIN")
        elif computerChoice == "Paper":
            print("TIE")
    elif userInput == "Scissors":
        print('You have selected Scissors and computer chose ' + computerChoice)
        if computerChoice == "Rock":
            print("YOU LOSE")
        elif computerChoice == "Paper":
            print("YOU WIN")
        elif computerChoice == "Scissors":
            print("TIE")
    
while True:
    ifState()
# print("Random generated is: ", random.choice(computerChoice))


