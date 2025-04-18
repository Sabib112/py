from abc import ABC, abstractmethod

class animal(ABC):

    @abstractmethod
    def move(self):
        pass

class dog(animal):

    def move(self):
        print("i am dog,i can bark")

class tiger(animal):

    def move(self):
        print("i am tiger,i can roar")

class cheetah(animal):

    def move(self):
        print("i am cheetah,i can run fast")

class hippo(animal):

    def move(self):
        print("i am hippo,i can swim")
    
    

d=dog()
t=tiger()
c=cheetah()
h=hippo()

d.move()
t.move()
c.move()
h.move()