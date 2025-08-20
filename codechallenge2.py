amount = int(input("Enter amount to deposit: "))

q = amount // 1000
amount = amount % 1000

w = amount // 500
amount = amount % 500

e = amount // 200
amount = amount % 200

r = amount // 100
amount = amount % 100

t = amount // 50
amount = amount % 50

y = amount // 20
amount = amount % 20

u = amount // 10
amount = amount % 10

i = amount // 5
amount = amount % 5

o = amount // 1
amount = amount % 1

print("P1000:", q)
print("P500:", w)
print("P200:", e)
print("P100:", r)
print("P50:", t)
print("P20:", y)
print("P10:", u)
print("P5:", i)
print("P1:", o)