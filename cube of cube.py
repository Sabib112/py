def cube(number):
    return number**3

def divisible_by_3(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print(divisible_by_3(8))
    