n= int (input("enter a number of rows"))
print("half pyramid with stars(*)")

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("")