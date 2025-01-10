temperature = float(input("Enter the temperature in Celsius: "))


if temperature > 25:
    print("It's warm! You can wear light clothes.")

elif 15 <= temperature <= 25:
    print("The weather is moderate. You can wear light clothes with a jacket.")
    
else:
    print("It's cold! You should wear warmer clothes like a jacket or sweater.")