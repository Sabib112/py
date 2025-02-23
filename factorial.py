def factorial(num):
    '''This function calculates the factorial of a number'''
    if num ==0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)
    
print(factorial(5))
print(factorial.__doc__)
print("hello")
