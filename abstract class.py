from abc import ABC, abstractmethod

class ABclass(ABC):
    def print(self,x):
        print("passed value is: ",x)
    
    @abstractmethod
    def task(self):
        print("i'm inside abstract class")

class test_class(ABclass):
    def task(self):
        print("i'm inside test class")


tst_obj=test_class()
tst_obj.task()
tst_obj.print(100)