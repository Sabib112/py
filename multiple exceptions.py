try:
    num1,num2= eval(input("enter two numbers separated by comma: "))
    result= num1/num2
    print(result)

except ZeroDivisionError:
    print("error division by error")
except SyntaxError:
    print("comma is missing. enter numbers separated by comma")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("finally done!")