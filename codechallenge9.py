# Countdown Simulator
print("Welcome to Countdown Simulator!")

countdown = eval(input("Enter a number for countdown: "))

import time
for j in range(countdown, 0, -1):
    print(j)
    time.sleep(1)
    
print("Lift Off!")
