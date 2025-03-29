class Parrot:
    species = "bird"  
    def __init__(self,name,age):
        self.name = name
        self.age = age

blu= Parrot("Blu", 10)
goofy= Parrot("Goofy", 5)

print("Blu is {}".format(blu.species))
print("Goofy is {}".format(goofy.species))

print("{} is {} years old" .format(blu.name,blu.age))
print("{} is {} years old" .format(goofy.name,goofy.age))