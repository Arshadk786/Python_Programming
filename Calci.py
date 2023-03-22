def Addition(first,second):
    print("\nAddition of "+str(first)+" and "+str(second)+" =",first+second)
    
def Subtraction(first,second):
    print("\nSubtraction of "+str(first)+" and "+str(second)+" =",first-second)
    
def Multiply(first,second):
    print("\nMultiplication of "+str(first)+" and "+str(second)+" =",first*second)
    
def Divide(first,second):
    print("\nDivision of "+str(first)+" and "+str(second)+" =",first//second)
    
def Remainder(first,second):
    print("\nRemainder of "+str(first)+" and "+str(second)+" =",first%second)
    
def Power(first,second):
    print("\nPower of "+str(first)+" and "+str(second)+" =",first**second)

first = int(input("Enter First number: "))
second = int(input("Enter Second number: "))
while 1:
    print("\n\n****************MENU****************")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Division")
    print("5.Remainder")
    print("6.Power")
    print("7.Exit")
    choose=int(input("Choose your option: "))

    if choose==1:
        Addition(first,second)
    elif choose==2:
        Subtraction(first,second)
    elif choose==3:
        Multiply(first,second)
    elif choose==4:
        Divide(first,second)
    elif choose==5:
        Remainder(first,second)
    elif choose==6:
        Power(first,second)
    elif choose==7:
        break
    else:
        print("\nInvalid Option")

    
