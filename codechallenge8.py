#Multiplication Maker
print("Welcome to Multiplication Table Maker!")

number = eval(input("Enter a number:"))

for j in range (1,11):
    result = number * j
    print(f"{number} x {j} = {result}")
