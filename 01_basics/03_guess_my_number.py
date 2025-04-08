# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

def main():
    # Generate the secret number at random between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99... 🎲")
    
    # Get the user's first guess
    guess = int(input("Enter a guess: "))
    
    # Keep prompting until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low 📉")
        else:
            print("Your guess is too high 📈")
        
        # Ask for a new guess
        print()  # Print an empty line for formatting
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
    
    # Once the correct guess is made, print the success message
    print(f"Congrats! The number was: {secret_number} 🎉")

if __name__ == '__main__':
    main()
