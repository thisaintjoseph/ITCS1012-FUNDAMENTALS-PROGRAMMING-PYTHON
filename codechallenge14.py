
name = input("Hi! what is your name?: ")
print("\nODD Number Compiler, type '0' to terminate the loop")

num = True
add = 0
odd = ""
while num == True:
    number = eval(input("Please enter a number"))
    if number % 2 == 1:
        print("ODD Number")
        odd += str(number) + ","
        add += number
        continue
    elif number == 0:
        print("Loop Terminated")
        break
    else:
        if number % 2 == 0:
            print("EVEN Number...skipping")
            continue
        else:
            print("Number Invalid")
            continue
print(f"Hi! {name}, The sum of all ODD Numbers is {add} ")
print(f"All the ODD Numbers you input is {odd}")