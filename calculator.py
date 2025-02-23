def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

print("please select an operation: ")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d.division")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("select operation to perform ranging a-d: ")

if choice == 'a':
    print("the sum of the two numbers is: ",add(num1,num2))
elif choice == "b":
    print("the difference of the two numbers is: ",sub(num1,num2))
elif choice == "c":
    print("the product of the two number is : ",multi(num1,num2))
elif choice == "d":
    print("the division of the two numbers is: ",div(num1,num2))
else:
    print("please select a valid operation")