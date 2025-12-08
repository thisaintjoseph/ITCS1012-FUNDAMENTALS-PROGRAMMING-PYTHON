

import random 

print("Number guess")

iba = random.randint(1, 3)

tries = 0

tuloy = True

while tuloy == True:
  
    num = int(eval(input("Input a number --> ")))

    tries += 1 

    if num == iba: 
        print("correct answer")
        print(f" you only took {tries} tries")
        break
    else:
        print("wrong answer")
        print("Continue")
        continue

