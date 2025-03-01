def calculate_change(total_amount, amount_paid):
    if amount_paid < total_amount:
        print("The payment is not enough to cover the total amount.")
    else:
        change = amount_paid - total_amount
        print(f"The customer will receive: ${change:.2f} in change.")


total_amount = float(input("Enter the total amount due: $"))
amount_paid = float(input("Enter the amount paid by the customer: $"))

calculate_change(total_amount, amount_paid)