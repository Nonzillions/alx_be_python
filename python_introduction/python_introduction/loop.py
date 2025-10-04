secret_number = 8
guess_count = 0

guess = int(input("Please enter a number between 0 and 10: "))

while guess != secret_number:
    guess_count += 1
    if guess > 10:
        print("You have entered a number greater than 10")
    else:
        print("Wrong guess, try again.")
    guess = int(input("Please enter a number between 0 and 10: "))

# when the loop ends, it means guess == secret_number
print(f"You guessed correctly in {guess_count} attempts!")



