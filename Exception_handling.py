print("Enter 2 numbers: ")
try:
    num1 = int(input())
    num2 = int(input())
    print(num1+num2)

except Exception as a:
    print(a)

finally:
    print("This is an important block of code that nedds to be executed")
