# create my own functions


def greeter(name):
    print(f"Hi {name}, how are you? ")

greeter('Joseph')
greeter('Nikka')
greeter('Jn')

def summation(x):
    sum = 0
    for y in range(x, 0, -1):
        sum += y
    print(f"the sum of {x}, is {sum}")



summation(30)
summation(19)

