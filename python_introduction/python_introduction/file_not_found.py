try:
    f = open ("file.txt")
except FileNotFoundError:
    print("File not found")


#ValueTooHighError
try:
    user_input = int(input("Enter a number betweeen 0 and 100: "))
    if user_input < 0 or user_input > 100:
        raise ValueError ("Number out of range")
except ValueError as e  :
    print("value too high: ", e)
else:
    print (f"You chose {user_input}")
