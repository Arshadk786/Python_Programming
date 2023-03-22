first_name = "Tony"
last_name = "Stark"
age = 51
is_genius = True
"""
superhero_name = input("What's your name? ")
print("Hello",superhero_name)
"""
'''old_age = int(input("Enter Your pre-pandemic age: "))
new_age = old_age + 2
print(new_age)'''

# number = 18
# num=str(number)
# print(num)
# print(type(num))

# Sum of Two numbers
# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# sum = first + second
# print("The Sum is",sum)

# # Strings
# name = "Arshad Khan"
# # print(name.upper())
# # print(name.lower())
# # print(name.find("a"))
# # print(name.replace("Arshad Khan", "Iron Man"))
# print("Khan" in name)

#Conversion of Datatypes
'''a= float(True)
print(str(a)+" and its type is "+str(type(a)))

b= bool(100)
print(str(b)+" and its type is "+str(type(b)))'''
#  Arithmetic Operators
"""print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(5//5)
print(5%5)
print(5**5)"""

# Shortcuts
"""i= 20
i+=40
print(i)
i-=40
print(i)
i*=40
print(i)
i/= 5
print(i)
i//=5
print(i)
i%= 5
print(i)
i**= 5
print(i)"""
# Operator Precedence
# print(5+6-2//7) # / has higher precendence compare to + & -

# Comparison Operator
'''print(3>2) 
print(3<2) 
print(3<=2) 
print(3>=2) 
print(3==3) 
print(3!=3) '''

# Logical Operator
'''print(3<2 or 2<3)
print(3<2 and 2<3)
print(not 3<2)'''

# If else
'''age = int(input("Enter your age: "))
if age>=18:
    print("You are an Adult and you can vote")
elif age<18 and age>3:
    print("You are in school")
else:
    print("You are a Child")'''
    
# Mini Calculator
"""first = int(input("Enter first number: "))
operator = input("Choose your operation (+,-,*,/,%): ")
second = int(input("Enter second number: "))
if operator == '+':
    print(first+second)
elif operator == '-':
    print(first-second)
elif operator == '*':
    print(first*second)
elif operator == '/':
    print(first/second)
elif operator == '%':
    print(first%second)
else:
    print("Invalid Operator")"""

# Range()
'''numbers = range(5,10,2)
print(numbers)'''

# Loops
"""While Loop"""
"""i=1
while i<=100:
    print(i)
    i+=1"""
    
# For Loop
'''for i in range(0,10,2):
    print(i)'''

# Lists[]
# list = [10,20,30,40,40,'h',"hello"]
# # list[0]= 5
# print(list[:5])
# # for i in list:
#     print(i)
'''list.append(90)

list.insert(4,50)
print(len(list))
print(list[::-1])'''
'''i=0
while i < len(list):
    print(list[i])
    i+=1'''

# Break & Continue 
'''companies = ["itc", "tata", "reliance","birla","adani"]

for com in companies:
    if com=="birla":
        continue
    print(com)'''

# Tuples()
'''t=(50,60,70,80,10,20,80,80,"helloo")
print(t.count(50))
print(t.index(80,4,7))
print(t)'''

# Sets{}
"""set = {10,20,30,40,"heloo",'hi',10,10}
print(set)
for i in set:
    print(i)"""
    
# Dictionaries
'''dict = {"physics": 80, "Chemistry":99, "Maths": 80}
print(dict)
print(dict["physics"])
'''
# Functions
def addup(first,second):
    print(first+second)

addup(2,3)
    