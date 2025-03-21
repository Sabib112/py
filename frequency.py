test_dict={'sabib':20,'ahian':10,'tairan':20,'ayman':5}

print("The original dictionary is : " + str(test_dict))

K=int(input("Enter the key to find the frequency: "))


res=0
for key in test_dict:
    if test_dict[key]==K:
        res+=1

print("The frequency of "+str(K)+" is : "+str(res))