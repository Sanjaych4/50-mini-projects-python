# Day 11: A guessing game (tossing a coin, throwing a dice, a number within a range)

import random

def guessing_game():
    print("Welcome to the guessing game!")
    print("Choose an option:")
    print("1. Guess a number")
    print("2. Toss a coin")
    print("3. Roll a dice")
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        low = 1
        high = 100
        secret_number = random.randint(low, high)
        print("I'm thinking of a number between {} and {}.".format(low, high))
        guess = None
        num_guesses = 0
        while guess != secret_number:
            try:
                guess = int(input("Guess a number: "))
                if guess < low or guess > high:
                    print("Your guess is outside the range!")
                elif guess < secret_number:
                    print("Too low!")
                    num_guesses += 1
                elif guess > secret_number:
                    print("Too high!")
                    num_guesses += 1
                else:
                    num_guesses += 1
                    print("You guessed it! It took you {} guesses.".format(num_guesses))
            except ValueError:
                print("Please enter a valid integer!")
    elif choice == "2":
        coin = random.choice(["heads", "tails"])
        guess = None
        num_guesses = 0
        while guess != coin:
            guess = input("Toss the coin (heads or tails): ")
            if guess.lower() != "heads" and guess.lower() != "tails":
                print("Please enter either 'heads' or 'tails'!")
            elif guess.lower() == coin:
                num_guesses += 1
                print("You guessed it! It took you {} guesses.".format(num_guesses))
            else:
                num_guesses += 1
                print("Sorry, it was {}! Guess again.".format(coin))
    elif choice == "3":
        dice = random.randint(1, 6)
        guess = None
        num_guesses = 0
        while guess != dice:
            try:
                guess = int(input("Roll the dice (1-6): "))
                if guess < 1 or guess > 6:
                    print("Please enter a number between 1 and 6!")
                elif guess < dice:
                    print("Too low!")
                    num_guesses += 1
                elif guess > dice:
                    print("Too high!")
                    num_guesses += 1
                else:
                    num_guesses += 1
                    print("You guessed it! It took you {} guesses.".format(num_guesses))
            except ValueError:
                print("Please enter a valid integer!")
    else:
        print("Invalid choice!")

#Function to start the guessing game
guessing_game()
