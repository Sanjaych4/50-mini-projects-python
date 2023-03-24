# Day 13: A word guessing game-2 (given a word, but letters are jumbled)

import random

#list
words = ["apple", "banana", "cherry", "orange", "grape", "melon", "pear", "kiwi"]

#Using random to select a word from the list
word = random.choice(words)

#jumble the letters of the word
jumbled_word = "".join(random.sample(word, len(word)))

print("Welcome to the Word Jumble Game!")
print("Unscramble the letters to make a word.")
print("The jumbled word is:", jumbled_word)

#prompt the user to guess the word
guess = input("Enter your guess: ").lower()

#check if the guess is correct
if guess == word:
    print("Congratulations! You guessed the word correctly.")
else:
    print("Sorry, your guess is incorrect. The word was:", word)
