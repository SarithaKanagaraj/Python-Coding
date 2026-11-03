import random
playing=True
number=str(random.randint(0,9))

print("I will generate a number between 0 and 9! You must guess the number!")
print("The game ends when you guess the number!")
while playing:
    guess=input("Enter your guess here:")
    if number==guess:
        print("Congratulations! You won!")
        print("The number is",number)
        break

    else:
        print("Your guess is not correct. Try again!\n")