from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time inside a variable
    current_date = datetime.now()
    
    # Format the date in "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print("Current date and time:", formatted_date)

def calculate_future_date(days: int):
    # get today's date
    today = datetime.today()
    # add the specified number of days
    future_date = today + timedelta(days=days)
    # return formatted date
    return future_date.strftime("%Y-%m-%d")

def main():
    display_current_datetime()
    days = int(input("Enter number of days to add to the current date: "))
    result = calculate_future_date(days)
    print("Future date:", result)

if __name__ == "__main__":
    main()
