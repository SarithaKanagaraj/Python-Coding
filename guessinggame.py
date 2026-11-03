# ================================
# NUMBER GUESSING GAME
# ================================

# ---------- SETTINGS (given to you) ----------
secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

while count<max_attempts and guess!=secret:
    guess=int(input("Your guess: "))
    count+=1

    # ---------- PART 2: win or not ----------
    if guess==secret:
        print(f"Congratulations! You guessed the secret number in {count} attempts!")
    else:
        if guess>secret:
            diff=guess-secret
        else:
            diff=secret-guess

        if diff>=20:
            print("Ice cold")
        elif diff>=10:
            print("Cold")
        elif diff>=5:
            print("Warm")
        else:
            print("Hot")

        remaining=max_attempts-count
        if remaining>0:
            print("Lives left: ", end="")
            for i in range(remaining):
                print("*", end=" ")
            print()

if guess != secret:
    print(f"\nGame over! The secret number was {secret}.")