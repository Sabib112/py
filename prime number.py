lower= int(input("enter the lower number"))
upper= int(input("enter the upper number"))
print("prime numbers between",lower,"and",upper,"are")

for i in range(lower,upper+1):
    if i >1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)