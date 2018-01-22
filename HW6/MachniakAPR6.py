#############################################################################################
#### 1) HW 6: Rock, Paper, Scissors
#### 2) Anthony Machniak
#### 3) 10/10/17
#### 4) This program will be a game of rock, paper, scissors between a person and the computer.
####    The interface will be through a menu.
#############################################################################################

import random


def main():
    playerChoice = 0
    
    wins = 0
    draws = 0
    losses = 0
    
    while playerChoice != 4:
        computerChoice = int(random.randint(1, 3))
        gameMenu()
        playerChoice = playerChoiceInput()
        
        while playerChoice >= 5 or playerChoice <= 0:
            print("ERROR: That is not a choice.")
            print("Please enter an integer.")
            gameMenu()
            playerChoice = playerChoiceInput()
        
        result = gameLogic(computerChoice, playerChoice)
        
        if result == 1:
            wins += 1
        elif result == 0:
            draws += 1
        elif result == -1:
            losses += 1
    
    print("Thank you for playing!")
    print("Wins = ", wins)
    print("Draws = ", draws)
    print("Losses = ", losses)


def gameLogic(computer, player):
    rockChoice = 1
    paperChoice = 2
    scissorsChoice = 3
    
    def win():
        print("The computer chose", computer)
        print("You Won!")
        return 1
    
    def tie():
        print("The computer chose", computer)
        print("Draw")
        return 0
    
    def loss():
        print("The computer chose", computer)
        print("You Lose")
        return -1
    
    if computer == rockChoice and player == rockChoice:
        return tie()
    elif computer == rockChoice and player == paperChoice:
        return win()
    elif computer == rockChoice and player == scissorsChoice:
        return loss()
    elif computer == paperChoice and player == rockChoice:
        return loss()
    elif computer == paperChoice and player == paperChoice:
        return tie()
    elif computer == paperChoice and player == scissorsChoice:
        return win()
    elif computer == scissorsChoice and player == rockChoice:
        return win()
    elif computer == scissorsChoice and player == paperChoice:
        return loss()
    elif computer == scissorsChoice and player == scissorsChoice:
        return tie()
    
    
def gameMenu():
    print(' MENU')
    print('1) Rock')
    print('2) Paper')
    print('3) Scissors')
    print('4) Quit')


def playerChoiceInput():
    while True:
        try:
            playerChoice = int(input("Enter your choice: "))
            return playerChoice
        except ValueError:
            print("ERROR: That is not a choice.")
            print("Please enter an integer.")
            gameMenu()


main()
