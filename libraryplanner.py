# Library Vist Planner Title
print("=====Library Visit Planner=====")

# Get the inputs
day=input("What day is it today? (Monday through Sunday)").strip().capitalize()
weather=input("What is the weather like today? (sunny,cloudy,rainy)").strip().lower()
is_book_return=input("Do you have to return the book? (yes/no)").strip().lower()

# Determine the day
if day=="Monday":
    print("It is",day,":start of the week")
elif day in("Tuesday", "Wednesday", "Thursday"):
    print("It is",day,":weekday")
elif day =="Friday":
    print("It is",day,":end of the week")
elif day in("Saturday", "Sunday"):
    print("It is",day,":weekend")
else:
    print("Unrecgonized day")

#  Operators
if weather=="sunny" and is_book_return=="yes":
    print("The weather is nice. Please return your book!")
elif weather=="rainy" or weather=="cloudy":
    print("Umbrella reminder: It might rain.")
else:
    print("No combination selected")

if not (is_book_return=="yes"):
    print("No book to return - have a great day!")


# Store variables
weekday=("Monday","Tuesday","Wednesday","Thursday","Friday")
weekend=("Saturday","Sunday")

# Combine the operators 
if not (weather=="sunny") and is_book_return=="yes":
    print("Don't go right now because of weather.")

# Print inputs
print("Inputs given\n","Day is",day,"\n Weather is", weather,"\n Book return status:",is_book_return)

# End of planner
print("=====Library Planner Complete!=====")
    
