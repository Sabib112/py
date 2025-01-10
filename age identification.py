age= int(input("Enter your age: "))

if age < 0:
    print("invalid age")

elif age<13:
    print("you are a child")

elif age<20:
    print("you are a teenager")

elif age<60:
    print("you are a adult")
else:
    print("you are an senior citizen")