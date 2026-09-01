# Beginning screen
print("=====================================")
print("Welcome to Custom Ride Builder")
print("=====================================")

# Choose an option
choice=int(input("Please select your ride: 1 for Bike, 2 for Car"))

# If bike is selected
if choice==1:
    bike_type=int(input("1 for Scooty, 2 for Mountain Bike"))
    if bike_type==1:
        print("You have selected Scooty")
        print("Top Speed: 80 km/h")
        print("Best for: City ride and main roads")
    else:
        print("You have selected Mountain Bike")
        print("Top Speed: 40 km/h")
        print("Best for: Rocky Terrain")
elif choice==2:
    car_type=int(input("1 for Sedan, 2 for SUV"))
    if car_type==1:
        print("You have selected Sedan")
        print("Seats: 5")
        print("Best for: Family Ride")
    else:
        print("You have selected SUV")
        print("Seats: 7")
        print("Best for: Offtrail Driving Adventures")
else:
    print("Invalid Input. Try Again.")

# Conclusion
print("=====================================")
print("You have finished Custom Ride Builder!")
print("=====================================")