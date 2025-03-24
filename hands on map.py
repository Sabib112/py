num1=[1,2,3,4]
num2=[5,6,7,8]

result=map(lambda x,y: x+y,num1,num2)
print(list(result))


def add(x,y):
    return x+y

result=map(add,num1,num2)
print(list(result))

def square(n):
    return n*n

result=map(square,num1)
print(list(result))