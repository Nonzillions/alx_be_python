#Zerodivision exception
num1 = int(input("Please enter a number: "))
num2 = int(input("Enter a second number: "))

try:
    division = num1/num2
    print(f"The result of the division is {division}")
except ZeroDivisionError:
    print("You have inputed a divisor of 0")
finally:
    print("Thank you")
