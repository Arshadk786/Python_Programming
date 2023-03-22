n = int(input("Enter matrix size: "))
b = bool(int(input("Enter 0 or 1: ")))
if b == True:
    for i in range(0, n):
        for j in range(i):
            print("*", end="")
        print()

elif b == False:
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print()
