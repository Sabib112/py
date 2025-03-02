try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError as ex:
    print("invalid input enter numbers only")
    