def decimal_to_binary(num):
    if num==0:
        return "0"
    binary=""
    while num>0:
        remainder=num%2
        binary=str(remainder)+binary
        num=num//2
        
    return binary

num=int(input("Enter the decimal number: "))
print(decimal_to_binary(num))