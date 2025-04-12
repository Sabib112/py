class myClass:
    __privateVar=27

    def __privateMethod(self):
        print("This is a private method")
        
    def hello(self):
        print("trying to print private variable",myClass.__privateVar)

c1= myClass()
c1.hello()
c1.__privateMethod()