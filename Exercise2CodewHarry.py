# Faulty calculator
operator = input("Enter Operator: ")
number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
if number_one == 45 and number_two == 3 and operator == '*':
    print(555)
elif number_one == 56 and number_two == 9 and operator == '+':
    print(77)
elif number_one == 5 and number_two == 6 and operator == '/':
    print(4)
elif operator == '+':
    print(number_one + number_two)
elif operator == '-':
    print(number_one - number_two)
elif operator == '/':
    print(number_one / number_two)
elif operator == '*':
    print(number_one * number_two)
