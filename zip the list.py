s1=['a','b','c']
s2=[1,2,3]
s3=list(zip(s1,s2))
print(s3)

lst1=[10,20,30,40]
lst2=[100,200,300,400]

for x,y in zip(lst1,lst2):
    print(x,y)