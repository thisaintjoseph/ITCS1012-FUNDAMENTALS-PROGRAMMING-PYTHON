
for j in range(1, 7, 1):
    for a in range(6, j, -1):
        print(" ", end=" ")
    for b in range(j, 0, -1):
        print(b, end=" ")
    for c in range(2, j + 1, 1):
        print(c, end=" ")
    print()

