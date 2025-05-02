class A:
    def __init__(self,a):
        self.a = a
    
    def __lt__(self,other):
        if (self.a < other.a):
            return f"{self.a} is less than {other.a}"
        else:
            return f"{self.a} is greater than {other.a}"
        
    def __eq__(self,other):
        if (self.a == other.a):
            return f"{self.a} is equal to {other.a}"
        else:
            return f"{self.a} is not equal to {other.a}"
    
ob1= A(5)
ob2= A(6)

print("Passed values are: ",ob1.a,ob2.a)
print(ob1<ob2)

ob3= A(5)
ob4= A(5)
print("Passed values are: ",ob3.a,ob4.a)
print(ob3==ob4)

ob5= A(5)
ob6= A(6)
print("Passed values are: ",ob5.a,ob6.a)
print(ob5==ob6)