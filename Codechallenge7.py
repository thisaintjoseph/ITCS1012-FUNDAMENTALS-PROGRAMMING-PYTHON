#summation
total = 0
for x in range(1, 11,1): 
    name = eval(input("Input a Number: "))
    if name % 2:
        total += name
print("The Sum of all odd number is",total) 
