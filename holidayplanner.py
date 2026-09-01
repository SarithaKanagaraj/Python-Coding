# Introduction
print("==================================")
print("Welcome to Holiday Planner!")
print("==================================")

# Ask for which holiday
holiday_break=int(input("1 for Winter break, 2 for summer break"))
if holiday_break==1:
    print("The break you have selected is Winter Break")
    activity=int(input("1 for watch a movie, 2 for play in the snow"))
    if activity==1:
        print("You have selected Watch a Movie")
        print("Take a blanket and get some snacks!")
    elif activity==2:
        print("You have selected Play in the Snow")
        print("Wear jacket, gloves, and call your friends to play")
    else:
        print("Invalid Input. Try Again")
elif holiday_break==2:
    print("The break you have selected is Summer Break")
    summer_activity=int(input("1 for go to the beach, 2 for trekking"))
    if summer_activity==1:
        print("You have selected Go to the Beach")
        print("Wear swimwear and have fun!")
    elif summer_activity==2:
        print("You have selected Trekking")
        print("Get proper gear, call some friends, and prepare for yor adventure!")
    else:
        print("Invalid Input. Try Again")
else:
    print("Invalid Input. Try Again")

print("==================================")
print("Holiday Planner Complete!")
print("==================================")
