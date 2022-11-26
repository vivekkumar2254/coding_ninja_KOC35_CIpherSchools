from random import randint Cnumber= randint(1,100)
print("Try to guess the number (between 1 and 100) in three guesses!\n")
score = 0

guess1 = int(input("Enter your 1st Guess:--\n"))
while True:
    if guess1 < Cnumber:
        print("your Guess was to small,have one more try.")
        break
    elif guess1 > Cnumber:
        print("your guess was too high, have one more try.")
        break
    else:
        print("Congrat's! Great job!")
        score = score+1
        break
guess2 = int(input("Enter your 2nd guess:--\n"))
while True:
        if guess2 < Cnumber:
            print("your guess was too high,have one more try.")
            break
        elif guess2 > Cnumber:
            print("your guess was too high,have one more try.")
            break

        else:
            print("congrat's! Great job!")
            score = score +1
            break


guess3 = int(input("Enter your 3rd guess:--\n"))
while True:
            if guess3 < Cnumber:
                print("Better luck next time!")
                break

            else:
                print("Congrat's! great job!")
                score = score + 1
                break
            print("your score is",score)

    