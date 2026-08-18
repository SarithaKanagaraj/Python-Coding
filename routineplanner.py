# Ask for the temperature outside
temperature=int(input("Enter Temperature in Celcius:"))

# Decide whether to play outside or stay inside
if temperature>20:
    play="Play outside"

else:
    play="Stay inside"

# Ask if there is rain outside
is_raining=input("IS it raining outside?(yes/no)")
if is_raining=="yes":
    print("Reminder: It is raining.")

# Ask for homework time in minutes
homework_time=int(input("Enter number of minutes for homework:"))
if homework_time>60:
    print("Take a study break every 60 minutes")
else:
    print("Do not take a break now.")

# Ask for free time to choose betweenn hobbies or planning
free_time=int(input("Enter your free time in minutes:"))
if free_time>30:
    activity="planning"
    print("Use your time for",activity)
else:
    activity="hobbies"
    print("Use your time for",activity)

# Print output
print("=====Final Summary=====")
print("Temperature:",temperature)
print("Chosen activity:",play)
print("Is it raining?",is_raining)
print("Homework Time:",homework_time)
print("Activity:",activity)
print("=======================")