# Ask questions for smart school planner
print("==== Smart School Planner ====")
print("Answer 3 quick questions and I will plan your day!\n")

day=input("What day is it today?(Monday to Sunday): ").strip().capitalize()
weather=input("What is the weather like?(sunny,rainy,cloudy) ").strip().lower()
homework=input("Do you have any homework?(yes/no)").strip().lower()

print()
print(f"==== Your Plan For {day} ====")
print("-"*35)

# Classify the day
if day in("Saturday", "Sunday"):
    print("Weekend Enjoy your free time!")
elif day=="Monday":
    print("First day of the week. Pack your weekly planner.")
elif day=="Friday":
    print("Last school day. Return library books.")
elif day in("Tuesday", "Wednesday", "Thursday"):
    print("Normal school day. Stay focused!")
else:
    print("Day not recognized.")

# Sunny and homework done
if weather=="sunny" and homework=="yes":
    print("After school, head to the park-great weather and homework is done!")

# Rainy or cloudy
if weather=="rainy" or weather=="cloudy":
    print("Weather tip: Pack your umbrella-it may get wet outside.")

# If homework is not done
if not (homework=="yes"):
    print("Homework not done. Finish before playing.")

# Combing the operators together
if weather=="rainy" and not (homework=="yes"):
    print("Stay in, finish your homework, then watch your favorite show.")
elif weather=="sunny" and homework=="yes" and not (day in("Saturday", "Sunday")):
    print("You are all set for an amazing school day!")
elif day in("Saturday", "Sunday") and weather=="sunny":
    print("Head outside and have fun!")
else:
    print("Take it one step at a time.")

print()
print("Plan Complete! Have a wonderful day!")