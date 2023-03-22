class Operations:
    def add(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
        return num1+num2
    
    def sub(self, num1, num2):
        return num1-num2
    
    def mul(self, num1, num2):
        return num1*num2
    
    def div(self, num1, num2):
        return num1//num2
num1 = int(input("Enter First Number: "))  
num2 = int(input("Enter Second Number: "))  
# o = Operations()
print(Operations().add(num1,num2)) 