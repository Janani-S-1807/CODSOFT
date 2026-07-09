import random

print("===== Rock Paper Scissors Game =====")

user_score = 0
computer_score = 0

while True:
    player = input("Enter rock, paper or scissors: ").lower()

    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("Your Choice :", player)
    print("Computer Choice :", computer)

    if player == computer:
        print("Result : Tie")

    elif player == "rock":
        if computer == "scissors":
            print("Result : You Win")
            user_score += 1
        else:
            print("Result : Computer Wins")
            computer_score += 1

    elif player == "paper":
        if computer == "rock":
            print("Result : You Win")
            user_score += 1
        else:
            print("Result : Computer Wins")
            computer_score += 1

    elif player == "scissors":
        if computer == "paper":
            print("Result : You Win")
            user_score += 1
        else:
            print("Result : Computer Wins")
            computer_score += 1

    print("Your Score :", user_score)
    print("Computer Score :", computer_score)

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nGame Over")
        print("Final Score")
        print("You :", user_score)
        print("Computer :", computer_score)
        break