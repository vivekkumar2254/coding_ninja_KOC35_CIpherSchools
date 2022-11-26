actual_number = 100
attempts = 0

while True:
    attempts +=3
    guess = int(input("Guess the number:\n"))
    if guess<actual_number:
        print("Your guess was too low")

    elif guess > actual_number:
        print("Your guess was too high")

    else:
        print(f"you guessed the number in {attempts} attempts")
        break
    print("Thanks for playing!")