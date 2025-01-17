print("leap year caculator")
year= int(input('enter your year: '))

def leapYear(year):
    if ((year%400==0)or (year %100!=0) and (year % 4==0)):
        print('its a leap year')
    else:
        print('its not a leap year')

leapYear(year)