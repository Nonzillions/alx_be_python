import random

secret_number = random.randint(0, 10)

while True:
    guess = int(input("Guess a number between 0 and 10: "))

    match guess:
        case g if g == secret_number:
            print("🎉 Congratulations, you guessed it!")
            break  # stop the loop once guessed correctly

        case g if g > secret_number:
            print("Oops, your guess is a bit high. Try again...")

        case g if g < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

        case _:
            print("❌ Invalid entry, please enter a number between 0 and 10.")


