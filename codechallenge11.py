print("\t\t     *",end='')
for j in range(1,12,1):
    for a in range(12 , j, -1):
        print("", end='  ')
    for b in range(1, j, 1):
        print("*", end = ' ')
    for c in range(1, j, 1):
        print("*", end=' ')
    print()

for j in range(1,12,1):
    for a in range(1, j, 1):
        print("", end='  ')
    for b in range(12, j, -1):
        print("*", end=' ')
    for c in range(12, j, -1):
        print("*", end = ' ')
    print()
print("\t\t     *",end='')