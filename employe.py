class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    
    def display(self):
        print("Name:",self.name)
        print("ID Number:",self.idnumber)
    
class employe(person):
    def __init__(self,name,idnumber,salary,post):
        super().__init__(name,idnumber)
        self.salary=salary
        self.post=post
    
    def display(self): 
        super().display()
        print("Salary:",self.salary)
        print("Post:",self.post)

a=employe("John",12345,50000,"Manager")
a.display()