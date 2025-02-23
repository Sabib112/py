def calculate_tip(bill, percentage):
    total = bill+bill*percentage*0.01
    total = round(total, 2)
    print(f"Pleses pay ${total}!")

calculate_tip(int(input("Enter the bill amount: ")), int(input("Enter the tip percentage: ")))