# Day 2: A letter, word, and sentence counter

# We are using the re module to count the number of letters and sentences using regular expressions
import re

# We are using the findall method to find all matches of the given pattern (in this case, [a-zA-Z] for letters and [.!?] 
# for sentence endings) and counting the length of the resulting list.
def count_letters_words_sentences(text):
    # Count letters 
    letter_count = len(re.findall('[a-zA-Z]', text))

    # Count words
    word_count = len(text.split())

    # Count sentences
    sentence_count = len(re.findall('[.!?]', text))

    return letter_count, word_count, sentence_count

text = input("Enter a sentence: ")
letter_count, word_count, sentence_count = count_letters_words_sentences(text)
print("Letter count:", letter_count)
print("Word count:", word_count)
print("Sentence count:", sentence_count)
