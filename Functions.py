# Funtions
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
n=int(input("Enter a number: "))
print("Factorial of",n,"=",fact(n))