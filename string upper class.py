class IOString:
    def __init__(self):
        self.str1=""
    
    def getString(self):
        self.str1= input("enter a string:  ")
    
    def printString(self):
        print('output:  ', self.str1.upper())

str1= IOString()
str1.getString()
str1.printString()