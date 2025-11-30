from Activity25_1 import *

name  = input("Whats is your name: ")

print(f"Welcome {name} to my File compiler")

t = True

while t == True:
    print("Select a program")
    print("A - activity1\nB - activity4\nC - activity5\nD - activity 6\nE - Exit")

    new = input("What program would you like to run: ").lower()

    if new == "a":
        activity1()
        continue
    elif new == "b":
        activity4()
        continue
    elif new == "c":
        activity5()
        continue
    elif new == "d":
        activity6()
    elif new == "e":
        print("Closed thanks!!")
        break
    else:
        print("Invalid, Try Again..")