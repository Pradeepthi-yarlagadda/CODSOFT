import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user = input("\nChoose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Score -> You:", user_score, "Computer:", computer_score)

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break