import random

userTally = 0
aiTally = 0

def ifState():
    computerGen = ['Rock', 'Paper', 'Scissors']

    global userTally
    global aiTally

    computerChoice = random.choice(computerGen)

    userInput = input("Please select your weapon of choice \n")
    
    # if/elif conditional statement used here
    if userInput == "Rock":
        print('You have selected Rock and computer chose ' + computerChoice)
        if computerChoice == "Paper":
            aiTally += 1
            print("YOU LOSE! AI Score is " + str(aiTally))
        elif computerChoice == "Scissors":
            userTally += 1
            print("YOU WIN! User Score is " + str(userTally))
        elif computerChoice == "Rock":
            print("TIE")
    elif userInput == "Paper":
        print('You have selected Paper and computer chose ' + computerChoice)
        if computerChoice == "Scissors":
            aiTally += 1
            print("YOU LOSE! AI Score is " + str(aiTally))
        elif computerChoice == "Rock":
            userTally += 1
            print("YOU WIN! User Score is " + str(userTally))
        elif computerChoice == "Paper":
            print("TIE")
    elif userInput == "Scissors":
        print('You have selected Scissors and computer chose ' + computerChoice)
        if computerChoice == "Rock":
            aiTally += 1
            print("YOU LOSE! AI Score is " + str(aiTally))
        elif computerChoice == "Paper":
            userTally += 1
            print("YOU WIN! User Score is " + str(userTally))
        elif computerChoice == "Scissors":
            print("TIE") 

# this True boolean allows for the program to continously run 
while True:
    ifState()