from datetime import datetime, timedelta

def add_days(start_date, days):
    date_format = "%Y-%m-%d"
    start_date_obj = datetime.strptime(start_date, date_format)
    end_date_obj = start_date_obj + timedelta(days=days)
    return end_date_obj.strftime(date_format)

def subtract_days(start_date, days):
    date_format = "%Y-%m-%d"
    start_date_obj = datetime.strptime(start_date, date_format)
    end_date_obj = start_date_obj - timedelta(days=days)
    return end_date_obj.strftime(date_format)

if __name__ == "__main__":
    print("Date Calculator")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    days = int(input("Enter the number of days to add or subtract: "))
    operation = input("Do you want to add or subtract days? (add/subtract): ")

    if operation == "add":
        result_date = add_days(start_date, days)
    elif operation == "subtract":
        result_date = subtract_days(start_date, days)
    else:
        print("Invalid operation")
        result_date = None

    if result_date:
        print(f"The resulting date is: {result_date}")

