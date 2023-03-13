import os

if(not os.path.exists("data")):
    os.mkdir("50DofPy")

for i in range(0, 50):
    os.mkdir(f"50DofPy/Day{i+1}")
    
