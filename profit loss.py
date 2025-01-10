actual_price= float(input("Enter your actual price: "))

selling_price= float(input("Enter your selling price: "))

if actual_price > selling_price:
    amount= actual_price - selling_price
    print(f"Loss: {amount}")

else:
    amount= selling_price-actual_price
    print(f"Profit: {amount}")