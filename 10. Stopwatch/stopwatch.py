# Day 10: A stopwatch (for specific seconds, minutes, etc.)

import time

def stopwatch(): #defining stopwatch function
    input("Press enter to start the stopwatch...")
    start_time = time.time()
    input("Press enter to stop the stopwatch...")
    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))

#Function to run stopwatch
stopwatch()
