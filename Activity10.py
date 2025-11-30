

print("WELCOME to Grocery!!")

name = input("What is your Name? ")
item = input("What item(Chicken/Pork): ")
number = eval(input("How many(1-10): "))
price = eval(input("How much? "))
PWD = input("are you PWD or Senior(Yes/No): ")
equal = number * price * .05
man = number * price
more = man - equal

print("---------------------------")

if pwd.lower() == "yes":
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",number,"\nPrice each: ",price,"\nTotal: ",man ,"\nDiscount:",equal,"\nTotal w/discount: ",more)
else
	print("Hello", name, "\nItem: ",item, "\nQuantity: ",number,"\nPrice each: ",price,"\nTotal: ",man ,"\nDiscount:","\nTotal w/discount: ",man)

