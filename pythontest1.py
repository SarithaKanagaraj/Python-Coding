secret_number=25
guess_1=int(input("Enter your first guess here."))
if guess_1<secret_number and guess_1>=secret_number-10 or guess_1>secret_number and guess_1<=secret_number+10:
    print("Hint: Warm!")
elif guess_1<secret_number and guess_1>=secret_number-15 or guess_1>secret_number and guess_1<=secret_number+15:
    print("Hint: Cold!")
elif guess_1<secret_number and guess_1>=secret_number-20 or guess_1>secret_number and guess_1<=secret_number+20:
    print("Hint: Ice Cold!")
elif guess_1<secret_number and guess_1>=secret_number-5 or guess_1>secret_number and guess_1>=secret_number+5:
    print("Hint: Hot!")
