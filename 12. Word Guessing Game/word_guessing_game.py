# Day 12: A word guessing game-1 (given a few letters of a word)

import random

#define a list of words for the game
word_list = ["Panacea", "Euphoria", "Luminous", "Epiphany", "Serene", "Chaos", "Labyrinthine", "Inquisitive", "Majestic", "Nebulous","Enigma", "Melancholy", "Resilience", "Ambivalent", "Exquisite", "Clandestine", "Indefatigable", "Ineffable", "Mellifluous", "Nostalgia","Effervescent", "Serendipity", "Ephemeral", "Supercilious", "Plethora", "Ethereal", "Quintessential", "Perfidious", "Ubiquitous", "Surreptitious","apple", "banana", "cherry", "durian", "elderberry", "fig", "grape", "honeydew", "indian gooseberry", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla bean", "watermelon", "xylocarp", "yellow watermelon", "zucchini"]
# Fun fact: I took help from ChatGPT to generate some difficult words to increase the difficulty of this game, so enjoy guessing ;)

#function to choose a word randomly from the list
def choose_word():
    return random.choice(word_list)

#function to generate a partially hidden version of the word
def partially_hide_word(word, reveal_count):
    #determine which letters to reveal
    reveal_indices = random.sample(range(len(word)), reveal_count)
    #create the partially hidden word
    hidden_word = ""
    for i in range(len(word)):
        if i in reveal_indices:
            hidden_word += word[i]
        else:
            hidden_word += "_"
    return hidden_word

#function to get the user's guess and validate it
def get_guess():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("Invalid guess. Please enter a single letter.")

#function to play the game
def play_game(difficulty):
    # choose a word and partially hide it
    word = choose_word()
    if difficulty == "easy":
        reveal_count = int(len(word) * 0.25)
    elif difficulty == "medium":
        reveal_count = int(len(word) * 0.5)
    else: # difficulty == "hard"
        reveal_count = int(len(word) * 0.75)
    hidden_word = partially_hide_word(word, reveal_count)

    #initialize the game state
    guesses_left = 6
    incorrect_guesses = []
    game_over = False

    #play the game
    while not game_over:
        #print the game state
        print("Guess the word:", hidden_word)
        print("Incorrect guesses:", ", ".join(incorrect_guesses))
        print("Guesses left:", guesses_left)

        #get the user's guess
        guess = get_guess()

        #check if the guess is correct
        if guess in word:
            #reveal the guessed letter in the hidden word
            new_hidden_word = ""
            for i in range(len(word)):
                if word[i] == guess:
                    new_hidden_word += guess
                else:
                    new_hidden_word += hidden_word[i]
            hidden_word = new_hidden_word
            #check if the game is won
            if hidden_word == word:
                print("Congratulations! You guessed the word:", word)
                game_over = True
        else:
            #add the incorrect guess to the list
            incorrect_guesses.append(guess)
            # decrement the guesses left
            guesses_left -= 1
            # check if the game is lost
            if guesses_left == 0:
                print("Sorry, you lost. The word was:", word)
                game_over = True

print("Welcome to the word guessing game!")
difficulty = input("Choose a difficulty level (easy, medium, hard): ")
play_game(difficulty)
