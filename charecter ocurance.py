string= input("enter the string: ")
char= input("enter the charecter: ")
i=0
count=0

while i <len(string):
    if (string[i] == char):
        count +=1

    i+= 1
    

print("the charecter",char,"occurs",count,"times in the string",string )