import random


def show_title():
    print("\n" + "=" * 45)
    print("          NUMBER GUESSING GAME")
    print("=" * 45)


def choose_difficulty():
    print("\nChoose your difficulty:")
    print("1. Easy   - Number 1 to 50   | 10 attempts")
    print("2. Medium - Number 1 to 100  | 7 attempts")
    print("3. Hard   - Number 1 to 200  | 5 attempts")

    while True:
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


def play_game():
    maximum, max_attempts, difficulty = choose_difficulty()

    secret_number = random.randint(1, maximum)
    attempts = 0

    print("\n" + "-" * 45)
    print(f"Difficulty: {difficulty}")
    print(f"I selected a number between 1 and {maximum}.")
    print(f"You have {max_attempts} attempts.")
    print("-" * 45)

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > maximum:
                print(f"Please enter a number between 1 and {maximum}.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")

            elif guess > secret_number:
                print("Too high! Try a lower number.")

            else:
                score = (max_attempts - attempts + 1) * 10

                print("\nCONGRATULATIONS!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Attempts used: {attempts}")
                print(f"Your score: {score}")

                return True

            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    print("\nGAME OVER!")
    print(f"The correct number was: {secret_number}")

    return False


def main():
    show_title()

    games_played = 0
    games_won = 0

    while True:
        result = play_game()

        games_played += 1

        if result:
            games_won += 1

        print("\n" + "=" * 45)
        print("             GAME STATISTICS")
        print("=" * 45)
        print(f"Games Played : {games_played}")
        print(f"Games Won    : {games_won}")
        print(f"Games Lost   : {games_played - games_won}")

        while True:
            again = input("\nDo you want to play again? (y/n): ").strip().lower()

            if again == "y" or again == "yes":
                break

            elif again == "n" or again == "no":
                print("\nThanks for playing!")
                print("Goodbye!")
                return

            else:
                print("Please enter y or n.")


if __name__ == "__main__":
    main()