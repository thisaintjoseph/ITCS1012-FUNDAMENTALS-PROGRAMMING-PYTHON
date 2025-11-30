#using for loop, ask user to input 10 numbers
#after input get the summation of all numbers

num = 0
for j in range(1,11,1):
    number = eval(input("Enter a number: "))
    num += number  
    print("The summation is", num )
print(num)
