import datetime

def list_months():
    for month in range(1, 13):
        month_name = datetime.date(1900, month, 1).strftime('%B')
        print(f"{month}: {month_name}")

if __name__ == "__main__":
    list_months()