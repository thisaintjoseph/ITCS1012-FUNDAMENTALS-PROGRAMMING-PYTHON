odd_num = 0

for j in range (1,11,1):
    number = eval(input(f"{j} - Enter a number: "))

    if number % 2 == 1:
        odd_num += number

print(f"The sum of the even number is {odd_num}")


