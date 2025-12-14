#Activities
from activity1 import activity1
from activity2 import activity2
from activity3 import activity3
from activity4 import activity4
from activity5 import activity5
from activity6 import activity6
from activity7 import activity7
from activity8 import activity8
from activity9 import activity9
from activity10 import activity10
from activity11 import activity11
from activity12 import activity12
from activity13 import activity13
from activity14 import activity14
from activity15 import activity15
from activity16 import activity16
from activity17 import activity17
from activity18 import activity18
from activity19 import activity19
from activity20 import activity20
from activity21 import activity21
from activity22 import activity22
from activity23 import activity23
from activity24 import activity24
from activity24_1 import activity24_1
from activity25 import activity25
from activity25_1 import activity25_1
from activity26 import activity26
from activity27 import activity27
from activity28 import activity28
#Code Challenges
from codechallenge1 import codechallenge1
from codechallenge2 import codechallenge2
from codechallenge3 import codechallenge3
from codechallenge4 import codechallenge4
from codechallenge5 import codechallenge5
from codechallenge6 import codechallenge6
from codechallenge7 import codechallenge7
from codechallenge8 import codechallenge8
from codechallenge9 import codechallenge9
from codechallenge10 import codechallenge10
from codechallenge11 import codechallenge11
from codechallenge12 import codechallenge12
from codechallenge13 import codechallenge13
from codechallenge14 import codechallenge14
from codechallenge15 import codechallenge15
from codechallenge16 import codechallenge16
#import standard modules for creative way for coding
import os 
import time #time is for delays
import sys  #for printing characters one by one
import itertools #for the spinner animation
import threading #to animate the spinner on the background

#Colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

#2. Helper functions (effects and border)

#A. Typing Effect
def type_effect(text, speed= 0.001):
    for j in text:
        sys.stdout.write(j)
        sys.stdout.flush()
        time.sleep(speed)
    print()

#B. Loading Dots
def loading_dots(text="Loading", dots=3, speed=0.4):
    print(text, end="")
    for j in range(dots):
        print(".", end="", flush=True)
        time.sleep(speed)
    print()

#Spinning Animation (shows a spinning character)
def spinner(seconds=2):
    done = False

    def animate():
        for j in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            print(f'\rLoading {j}', end='', flush=True)
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(seconds)
    done = True
    print("\rDone!     ")

#border
def border10():
    for i in range(40):
        print("█", end="", flush=True)
        time.sleep(0.005)
    print()
# it prints a horizontal line of 40 blocks with a tiny delay


#Ask the name of the user
name  = (input("Whats is your name: "))
os.system('cls')

#Greet the user
type_effect(f"Welcome {name}, to my File Compiler :)")

#MAIN PROGRAM LOOP
#using while loop for our code to not break
while True: #(Using WHILE TRUE, the menu will not break until the user break it)
    border10()
    type_effect(" MAIN MENU ".center(40))
    border10()
    type_effect("A - Activities\nB - CodeChallenges\nE - Exit")
    border10()

    #putting variables

    new = input(YELLOW + "What program would you like to run: "+ RESET).upper()
    #Activities
    os.system('cls')
    if new == "A":
        while True:
            border10()
            type_effect(" ACTIVITIES MENU ".center(40))
            border10()
            
            type_effect("1 - Activity 1-5")  #creating a file of activities to be organized
            type_effect("2 - Activity 6-10")
            type_effect("3 - Activity 11-15")
            type_effect("4 - Activity 16-20")
            type_effect("5 - Activity 20-25")
            type_effect("6 - Activity 26-28")
            type_effect("7 - Search Activity")
            type_effect("0 - Back")
            border10()
            
            pick = input(GREEN + "Enter a number: "+ RESET)
            os.system('cls')
            #Search feature for the Activities
            if pick == '7':
                search_num = input(GREEN + "Enter Activity Number (1-28): " + RESET)

                if search_num.isdigit():
                    search_num = int(search_num)

                    if 1 <= search_num <= 28:
                        type_effect(f"Searching for Activity {search_num}...")
                        loading_dots("Starting")
                        globals()[f"activity{search_num}"]()
                    else:
                        type_effect("Invalid Activity Number")
                else:
                    type_effect("Please enter a valid number")
                continue

            if pick == '1':
                while True:
                    border10()
                    type_effect(" ACTIVITIES 1-5 ".center(40))
                    border10()

                    type_effect("1 - Activity 1\n2 - Activity 2\n3 - Activity 3\n4 - Activity 4\n5 - Activity 5\n0- Back ")
                    border10()

                    num1 = (input(GREEN + "Enter a number you want to open: " + RESET))
                    os.system('cls')
                    
                    if num1 == '1':
                        type_effect("Now Running Activity 1\n")
                        loading_dots("Starting")
                        activity1()
                        continue
                        os.system('cls')

                    elif num1 == '2':
                        type_effect("Now Running Activity 2")
                        spinner(2)
                        activity2()
                        continue
                        os.system('cls')

                    elif num1 == '3':
                        type_effect("Now Running Activity 3")
                        loading_dots("Starting")
                        activity3()
                        continue
                        os.system('cls')

                    elif num1 == '4':
                        type_effect("Now Running Activity 4")
                        spinner(2)
                        activity4()
                        continue
                        os.system('cls')

                    elif num1 == '5':
                        type_effect("Now Running Activity 5")
                        loading_dots("Starting")
                        activity5()
                        continue
                        os.system('cls')

                    elif num1 == '0':
                        break
                        os.system('cls')

                    
                    #like the first code, copy/paste it and edit the variables
            if pick == '2':
                while True:
                    border10()
                    type_effect(" ACTIVITIES 6-10 ".center(40))
                    border10()
                    
                    type_effect("1 - Activity 6\n2 - Activity 7\n3 - Activity 8\n4 - Activity 9\n5 - Activity 10\n0 - Back ")
                    border10()

                    num2 = (input(GREEN + "Enter a number you want to open: " + RESET))
                    os.system('cls')

                    if num2 == '1':
                        type_effect("Now Running Activity 6\n")
                        spinner(2)
                        activity6()
                        continue
                        os.system('cls')

                    elif num2 == '2':
                        type_effect("Now Running Activity 7\n")
                        loading_dots("Starting")
                        activity7()
                        continue
                        os.system('cls')

                    elif num2 == '3':
                        type_effect("Now Running Activity 8\n")
                        spinner(2)
                        activity8()
                        continue
                        os.system('cls')

                    elif num2 == '4':
                        type_effect("Now Running Activity 9\n")
                        loading_dots("Starting")                
                        activity9()
                        continue
                        os.system('cls')

                    elif num2 == '5':
                        type_effect("Opening Activity 10\n")
                        spinner(2)
                        activity10()
                        continue
                        os.system('cls')

                    elif num2 == '0':
                        break
                        os.system('cls')
                    
                
            #same on this 
            if pick == '3':
                while True:
                    border10()
                    type_effect(" ACTIVITIES 11-15 ".center(40))
                    border10()

                    type_effect("1 - Activity 11\n2 - Activity 12\n3 - Activity 13\n4 - Activity 14\n5 - Activity 15\n0 - Back ")
                    border10()

                    num3 = (input(GREEN + "Enter a number you want to open: " + RESET))
                    os.system('cls')

                    if num3 == '1':
                        type_effect("Now Running Activity 11\n")
                        loading_dots("Starting")
                        activity11()
                        continue
                        os.system('cls')

                    elif num3 == '2':
                        type_effect("Now Running Activity 12\n")
                        spinner(2)
                        activity12()
                        continue
                        os.system('cls')

                    elif num3 == '3':
                        type_effect("Now Running Activity 13\n")
                        loading_dots("Starting")
                        activity13()
                        continue
                        os.system('cls')

                    elif num3 == '4':
                        type_effect("Now Running Activity 14\n")
                        spinner(2)                
                        activity14()
                        continue
                        os.system('cls')

                    elif num3 == '5':
                        type_effect("Opening Activity 15\n")
                        loading_dots("Starting")
                        activity15()
                        continue
                        os.system('cls')

                    elif num3 == '0':
                        break
                        os.system('cls')
                
                
            
            if pick == '4':
                while True:
                    border10()
                    type_effect(" ACTIVITIES 16-20 ".center(40))
                    border10()
                    
                    type_effect("1 - Activity 16\n2 - Activity 17\n3 - Activity 18\n4 - Activity 19\n5 - Activity 20\n0 - Back ")
                    border10()
                    num4 = (input("Enter a number you want to open: "))
                    os.system('cls')

                    if num4 == '1':
                        type_effect("Now Running Activity 16\n")
                        spinner(2)
                        activity16()
                        continue
                        os.system('cls')

                    elif num4 == '2':
                        type_effect("Now Running Activity 17\n")
                        loading_dots("Starting")
                        activity17()
                        continue
                        os.system('cls')

                    elif num4 == '3':
                        type_effect("Now Running Activity 18\n")
                        spinner(2)
                        activity18()
                        continue
                        os.system('cls')

                    elif num4 == '4':
                        type_effect("Now Running Activity 19\n")
                        loading_dots("Starting")                
                        activity19()
                        continue
                        os.system('cls')

                    elif num4 == '5':
                        type_effect("Opening Activity 20\n")
                        spinner(2)
                        activity20()
                        continue
                        os.system('cls')

                    elif num4 == '0':
                        break
                        os.system('cls')

                
            #ALSO ON THIS
            if pick == '5':
                while True:
                    border10()
                    type_effect(" ACTIVITIES 21-25 ".center(40))
                    border10()
                    type_effect("1 - Activity 21\n2 - Activity 22\n3 - Activity 23\n4 - Activity 24\n5 - Activity 25\n0 - Back ")
                    border10()

                    num5 = (input("Enter a number you want to open: "))
                    os.system('cls')

                    if num5 == '1':
                        type_effect("Now Running Activity 21\n")
                        loading_dots("Starting")
                        activity21()
                        continue
                        os.system('cls')

                    elif num5 == '2':
                        type_effect("Now Running Activity 22\n")
                        spinner(2)
                        activity22()
                        continue
                        os.system('cls')

                    elif num5 == '3':
                        type_effect("Now Running Activity 23\n")
                        loading_dots("Starting")
                        activity23()
                        continue
                        os.system('cls')

                    elif num5 == '4':
                        type_effect("Now Running Activity 24\n")
                        spinner(2)                
                        activity24()
                        continue
                        os.system('cls')

                    elif num5 == '5':
                        type_effect("Opening Activity 25\n")
                        loading_dots("Starting")
                        activity25()
                        continue
                        os.system('cls')

                    elif num5 == '0':
                        break
                        os.system('cls')
                
                
            if pick == '6':
                while True:
                    border10()
                    type_effect(" ACTIVITIES 26-28 ".center(40))
                    border10()
                    type_effect("1 - Activity 26\n2 - Activity 27\n3 - Activity 28\n0 - Back ")
                    border10()

                    num6 = (input("Enter a number you want to open: "))
                    os.system('cls')

                    if num6 == '1':
                        type_effect("Now Running Activity 26\n")
                        spinner(2)
                        activity26()
                        continue
                        os.system('cls')

                    elif num6 == '2':
                        type_effect("Now Running Activity 27\n")
                        loading_dots("Starting")
                        activity27()
                        continue
                        os.system('cls')

                    elif num6 == '3':
                        type_effect("Now Running Activity 28\n")
                        spinner(2)
                        activity28()
                        continue
                        os.system('cls')

                    elif num6 == '0':
                        break
                        os.system('cls')                      
            elif pick == '0':
                break
            #I Added a new selection which is the "0" to have a more creative way of going back and forth on a certain file
            
        #Code Challenges from 1 to 16, same method that I use on the Activities
    elif new == "B":
        while True:
            border10()
            type_effect(" CODE CHALLENGES MENU ".center(40))
            border10()

            type_effect("1 - Code Challenges 1-5")
            type_effect("2 - Code Challenges 6-10")
            type_effect("3 - Code Challenges 11-16")
            type_effect("4 - Search Code Challenge")
            type_effect("0 - Back")
            border10()

            pick1 = input(BLUE +"Enter a Number: " + RESET)
            os.system('cls')
            #search menu for code challenges
            if pick1 == '4':
                search_code = input(BLUE + "Enter Code Challenge Number (1-16): " + RESET)

                if search_code.isdigit():
                    search_code = int(search_code)

                    if 1 <= search_code <= 16:
                        type_effect(f"Searching for Code Challenge {search_code}...")
                        loading_dots("Starting")
                        globals()[f"codechallenge{search_code}"]()
                    else:
                        type_effect("Invalid Code Challenge Number")
                else:
                    type_effect("Please enter a valid number")
                continue

            if pick1 == '1':
                while True:
                    border10()
                    type_effect(" CODE CHALLENGES 1-5 ".center(40))
                    border10()

                    type_effect("1 - Code Challenge 1\n2 - Code Challenge 2\n3 - Code Challenge 3\n4 - Code Challenge 4\n5 - Code Challenge 5\n0 - Back ")
                    border10()

                    code1 = (input(BLUE + "Enter a number you want to open: " + RESET))
                    os.system('cls')

                    if code1 == '1':
                        type_effect("Now Running Code Challenge #1")
                        loading_dots("Starting")
                        codechallenge1()
                        continue
                        os.system('cls')

                    elif code1 == '2':
                        type_effect("Now Running Code Challenge #2")
                        loading_dots("Starting")
                        codechallenge2()
                        continue
                        os.system('cls')

                    elif code1 == '3':
                        type_effect("Now Running Code Challenge #3")
                        loading_dots("Starting")
                        codechallenge3()
                        continue
                        os.system('cls')

                    elif code1 == '4':
                        type_effect("Now Running Code Challenge #4")
                        loading_dots("Starting")
                        codechallenge4()
                        continue
                        os.system('cls')

                    elif code1 == '5':
                        type_effect("Now Running Code Challenge #5")
                        loading_dots("Starting")
                        codechallenge5()
                        continue
                        os.system('cls')

                    elif code1 == '0':
                        break
                        os.system('cls')

            if pick1 == '2':
                while True:
                    border10()
                    type_effect(" CODE CHALLENGES 6-10 ".center(40))
                    border10()
                    
                    type_effect("1 - Code Challenge 6\n2 - Code Challenge 7\n3 - Code Challenge 8\n4 - Code Challenge 9\n5 - Code Challenge 10\n0 - Back ")
                    border10()

                    code2 = (input(BLUE + "Enter a number you want to open: " + RESET))
                    os.system('cls')

                    if code2 == '1':
                        type_effect("Now Running Code Challenge #6")
                        loading_dots("Starting")
                        codechallenge6()
                        continue
                        os.system('cls')

                    elif code2 == '2':
                        type_effect("Now Running Code Challenge #7")
                        loading_dots("Starting")
                        codechallenge7()
                        continue
                        os.system('cls')

                    elif code2 == '3':
                        type_effect("Now Running Code Challenge #8")
                        loading_dots("Starting")
                        codechallenge8()
                        continue
                        os.system('cls')

                    elif code2 == '4':
                        type_effect("Now Running Code Challenge #9")
                        loading_dots("Starting")
                        codechallenge9()
                        continue
                        os.system('cls')

                    elif code2 == '5':
                        type_effect("Now Running Code Challenge #10")
                        loading_dots("Starting")
                        codechallenge10()
                        continue
                        os.system('cls')

                    elif code2 == '0':
                        break
                        os.system('cls')

            if pick1 == '3':
                while True:
                    border10()
                    type_effect(" CODE CHALLENGES 11-16 ".center(40))
                    border10()

                    type_effect("1 - Code Challenge 11\n2 - Code Challenge 12\n3 - Code Challenge 13\n4 - Code Challenge 14\n5 - Code Challenge 15\n6 - Code Challenge 16\n0 - Back ")
                    border10()

                    code3 = (input(BLUE + "Enter a number you want to open: " + RESET))
                    os.system('cls')

                    if code3 == '1':
                        type_effect("Now Running Code Challenge #11")
                        loading_dots("Starting")
                        codechallenge11()
                        continue
                        os.system('cls')

                    elif code3 == '2':
                        type_effect("Now Running Code Challenge #12")
                        loading_dots("Starting")
                        codechallenge12()
                        continue
                        os.system('cls')

                    elif code3 == '3':
                        type_effect("Now Running Code Challenge #13")
                        loading_dots("Starting")
                        codechallenge13()
                        continue
                        os.system('cls')

                    elif code3 == '4':
                        type_effect("Now Running Code Challenge #14")
                        loading_dots("Starting")
                        codechallenge14()
                        continue
                        os.system('cls')

                    elif code3 == '5':
                        type_effect("Now Running Code Challenge #15")
                        loading_dots("Starting")
                        codechallenge15()
                        continue
                        os.system('cls')

                    elif code3 == '6':
                        type_effect("Now Running Code Challenge #16")
                        loading_dots("Starting")
                        codechallenge16()
                        continue
                        os.system('cls')

                    elif code3 == '0':
                        break
                        os.system('cls')

            if pick1 == '0':
                break


    elif new == 'E':
        type_effect("Closed, thanks for coming bye :)")
        break

    else: 
        type_effect("Error, try again")
        break
    