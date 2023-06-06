import random

def rock_paper_scissors():
    scores = {"player": 0, "computer": 0}

    while True:
        user_input = input("Enter a choice (rock, paper, scissors): ")
        actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(actions)
        print(f"\nYou have chosen {user_input}. The computer chose {computer_action}")

        if user_input == computer_action:
            print(f"Both selected {user_input}. It's a tie!")

        elif user_input == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
                scores["player"] += 1
            else:
                print("Paper covers rock! You lose.")
                scores["computer"] += 1

        elif user_input == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
                scores["player"] += 1
            else:
                print("Scissors cuts paper! You lose.")
                scores["computer"] += 1

        elif user_input == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
                scores["player"] += 1
            else:
                print("Rock smashes scissors! You lose.")
                scores["computer"] += 1

        print(f"Player: {scores['player']} - Computer: {scores['computer']}")

        repeat = input("Play again? (yes / no): ")

        if repeat != "yes":
            if scores["player"] > scores["computer"]:
                print("Congratulations! You won the game!")
            elif scores["player"] < scores["computer"]:
                print("Sorry! You lost the game!")
            else:
                print("The game is tied!")
            break
        
rock_paper_scissors()