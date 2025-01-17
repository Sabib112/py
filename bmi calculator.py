height= float(input("enter your height "))
weight= float(input("enter your weight "))

bmi= weight/(height/100)**2
bmi= round(bmi,2)

print("your bmi is : ",bmi)

if bmi<18.5:
    print("you are underweight")

elif bmi>=18.5 and bmi <=24.9:
    print('you are normal weight')
elif bmi>=25 and bmi <=29.9:
    print('you are overweight')
else:
    print('you are obese')