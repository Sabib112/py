num=int(input("enter a number"))

sum=0

for i in  range(1, num+1, 2):
    sum= sum+i
    print(i,",sum",sum)


print("sum = ",sum)
