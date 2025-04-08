import random

NUM_ROUNDS = 5  # Number of rounds to play
score = 0

def main():
    global score
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for round_num in range(1, NUM_ROUNDS + 1):
        # Generate random numbers
        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)

        print(f"Round {round_num}")
        print(f"Your number is {user_number}")
        
        # Get user input
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Validate user input
        while guess not in ["higher", "lower"]:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Check if the guess is correct
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")
        print()  # Blank line between rounds

    # Game over, display result
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
