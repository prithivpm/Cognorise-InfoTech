import random

class Game:
    def __init__(self):
        self.us = 0
        self.com = 0
        self.choices = ['rock', 'paper', 'scissors']

    def get_usr_choice(self):
        while True:
            c = input("rock, paper, or scissors: ").lower()
            if c in self.choices:
                return c
            else:
                print("Invalid choice! Choose again.")

    def get_com_choice(self):
        return random.choice(self.choices)

    def winner(self, usr, com):
        if usr == com:
            return "tie"
        elif (usr == 'rock' and com == 'scissors') or \
             (usr == 'paper' and com == 'rock') or \
             (usr == 'scissors' and com == 'paper'):
            return "user"
        else:
            return "computer"

    def update_score(self, w):
        if w == "user":
            self.us += 1
        elif w == "computer":
            self.com += 1

    def display(self, usr, com, w):
        print(f"\nYou chose {usr}, computer chose {com}.")
        if w == "tie":
            print("It's a tie!")
        elif w == "user":
            print("You win!")
        else:
            print("Computer wins!")
        print(f"Score: You - {self.us}, Computer - {self.com}")

    def play_again(self):
        return input("Play again? (yes/no): ").lower() == "yes"

def main():
    game = Game()
    print("Rock, Paper, Scissors!")
    
    while True:
        usr_choice = game.get_usr_choice()
        com_choice = game.get_com_choice()

        win = game.winner(usr_choice, com_choice)
        game.update_score(win)
        game.display(usr_choice, com_choice, win)

        if not game.play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
