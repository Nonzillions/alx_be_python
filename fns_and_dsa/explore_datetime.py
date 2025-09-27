import datetime
import datetime

def display_current_datetime():
    # Save the current date and time inside a variable
    current_date = datetime.datetime.now()
    
    # Format the date in "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print("Current date and time:", formatted_date)

# Call the function
display_current_datetime()

def calculate_future_date(days: int):
    # get today's date
    today = datetime.date.today()
    # add the specified number of days
    future_date = today + datetime.timedelta(days=days)
    # return formatted date
    return future_date.strftime("%Y-%m-%d")

def main():
    # prompt user for number of days
    days = int(input("Enter number of days to add: "))
    result = calculate_future_date(days)
    print("Future date:", result)

if __name__ == "__main__":
    main()
