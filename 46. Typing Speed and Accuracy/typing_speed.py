# Day 46: Check the typing speed and accuracy

import time

def typing_test():
    text = input("Type the following sentence: 'The quick brown fox jumps over the lazy dog.'\n")

    start_time = time.time()
    typed_text = input("Type the above sentence:\n")
    end_time = time.time()
    elapsed_time = end_time - start_time
    typing_speed = len(text) / elapsed_time

    errors = 0
    for i in range(len(text)):
        if text[i] != typed_text[i]:
            errors += 1
    accuracy = (len(text) - errors) / len(text) * 100

    print(f"Time taken: {elapsed_time:.2f}s")
    print(f"Typing speed: {typing_speed:.2f} characters per second")
    print(f"Accuracy: {accuracy:.2f}%")
    
typing_test()

