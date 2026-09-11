#Chore Checklist Countdown

# Set today's total number of chores
total_chores=4
original_count=total_chores
print(f"You have {original_count} chores to finish today!\n")


# Count number of chores
chores_completed=0
chores_num=1

# While loop
while chores_num<=total_chores:
   
# Conditionals
    if chores_num==1: 
        next_chore="Make your bed"
        print(next_chore)
    elif chores_num==2: next_chore="Feed your pet"
    elif chores_num==3: next_chore="Take out the trash"
    else: next_chore="Wash the dishes"
    answer=input(f"Have you finished {next_chore}?(yes/no)")
    # Only move on when previous chore is complete
    if answer=="yes":
        chores_completed+=1
        chores_num+=1
        print("Great job!")
    else:
        print("Please finish your task before moving on.")

# Print how many chores are left
print("Chores remaining:",total_chores-chores_completed)
print()

# Prints after every chore is done
print("==========Checklist Complete==========")
print("Great job finishing today's chores!\n")

# Infinite loop 
print("Let's look at an infinte loop.")
test_value=0
safety_counter=0
while test_value==0:
    print("This condition never changes, so it will print forever!")
    safety_counter+=1
    if safety_counter==3:
        print("(Stopping here on purpose)")
        break

# Final Result
print("===== CHORE CHECKLIST SUMMARY=====")
print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned Today:", original_count)
print("Chores Completed:", chores_completed)
print("Chores Remaining:", total_chores - chores_completed)
print("======================================")