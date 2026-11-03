import random
while True:
    user_action=input("Enter a choice: (rock, paper, scissors):")
    possible_actions=["rock","paper","scissors"]
    computer_actions=random.choice(possible_actions)
    print(f"\n You chose {user_action}, computer chose {computer_actions}.\n")
    if user_action==computer_actions:
        print(f"Both players selected {user_action}. You tied!")
    elif user_action=="rock":
        if computer_actions=="scissors":
            print("Rock beats scissors. You win!")
        else:
            print("Paper beats rock. You lose!")
    elif user_action=="paper":
        if computer_actions=="rock":
            print("Paper beats rock. You win!")
        else:
            print("Scissors beat paper. You lose!")
    elif user_action=="scissors":
        if computer_actions=="paper":
            print("Scissors beat paper. You win!")
        else:
            print("Rock beats scissors. You lose!")

    play_again=input("Play again?(y/n)")
    if play_again!="y":
        break