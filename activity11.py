

temp = eval(input("what is the temperature now? "))

if temp <= 0:
    print("the temp is so cold")
elif temp >= 1 and temp <= 20:
    print("The temp is cold")
elif temp >= 21 and temp <= 30:
    print("The temp is lookwarm")
elif temp >= 31 and temp <= 40:
    print("The temp is warm")
elif temp >= 41 and temp <= 50:
    print("The temp is hot")
elif temp >= 51:
    print("The temp is boiling hot")
else:
    print("unrecognizable")