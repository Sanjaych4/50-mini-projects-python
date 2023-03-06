# importing os module
import os

# script that creates 50 Folders for the 50 days of Python Projects
if(not os.path.exists("py")):
    os.mkdir("50DofPy")

for i in range(0, 50):
    os.mkdir(f"50DofPy/Day{i+1}")
    
