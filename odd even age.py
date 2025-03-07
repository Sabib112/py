def check_age(age):
    try:
    
        if not age.isdigit():
            raise ValueError("Invalid input! Age must be a whole number.")
        
        age = int(age)  
        
        
        if age < 0 or age > 120:
            raise ValueError("Invalid age! Age must be between 0 and 120.")
        
        
        if age % 2 == 0:
            print("Age is even")
        else:
            print("Age is odd")
    
    except ValueError as v:
        print("Error:", v)


age = input("Enter your age: ")
check_age(age)