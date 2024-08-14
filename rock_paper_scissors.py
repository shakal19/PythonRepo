import random


def computer_move() -> str:
    """
    Makes computer move.
    """
    moves = ["rock", "paper", "scissors"]
    computer_choice = random.choice(moves)
    return computer_choice


def user_move():
    """
    Creates user's move.
    """
    while True:
        try:
            user_choice = int(
                input("Enter your choice:\n 0 - rock\n 1 - paper\n 2 - scissors\nYour choice is: ")
            )
            if user_choice in [0, 1, 2]:
                break
            else:
                print("Enter only 0, 1 or 2!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if user_choice == 0:
        return "rock"
    elif user_choice == 1:
        return "paper"
    else:
        return "scissors"


def game() -> None:
    """
    Game logic.
    """
    user_choice = user_move()
    computer_choice = computer_move()

    if user_choice == computer_choice:
        print("DRAW!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("YOU WIN!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("YOU LOST!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("YOU LOST!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("YOU WON!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("YOU WON!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("YOU LOST!")


def restart_game() -> bool:
    """
    Game restarting function
    """

    choice = input("Do you want to restart the game? (Y/n): ")
    if choice.lower() == "y":
        return True
    else:
        return False


def game_loop() -> None:
    """
    Game loop function.
    If you enter 'n', game stops.
    """
    game()
    while True:

        if restart_game() == True:
            game()
        else:
            print("THE END!")
            break


def main() -> None:
    """
    Driver function
    """
    game_loop()


if __name__ == "__main__":
    main()
