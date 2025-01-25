unit= int(input("enter the units you consumed: "))

if unit<50:
    amount = unit*5
    vat=50
elif unit<=100:
    amount= unit*7
    vat=100
elif unit<200:
    amount= unit*10
    vat=200
else:
    amount=unit*15
    vat=300

total= amount+vat
print(total)
