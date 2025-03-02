def check_age (age):
    try:
        if age <0 or age > 120:
            raise ValueError("invalid age!")
        if age % 2 == 0:
            print("age is even")
        else:
            print("age is odd")
    except ValueError as v:
        print("error: ",v)
    
age= int(input("enter your age: "))
check_age(age)