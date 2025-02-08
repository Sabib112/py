r= int(input("enter the number of rows"))
n=1

print('floys triange with numbers')

for i in range(1,r+1):
    for j in range(1, i+1):
        print(n, end=" ")
        n+=1
    print()