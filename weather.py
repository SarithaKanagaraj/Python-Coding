# Ask for today's temperature
temperature=int(input("Enter today's temperature in celsius:"))

# Decide between a jacket and a Tshirt
if temperature<20:
    outfit="jacket"
    print("It is cold today.")
    print("Wear a",outfit)
else:
    outfit="t-shirt"
    print("It is warm today.")
    print("Wear a",outfit)

# Ask if it is raining
is_raining=input("Is it raining today? (yes/no)")

# Add an umbrella reminder only if it is raining
if is_raining=="yes":
    print("Bring an umbrella!")

# Ask for the wind speed
wind_speed=int(input("Enter today's wind speed here in km/hr:"))

# Decide whether to wear a windbreaker
if wind_speed>30:
    needs_windbreaker="yes"
    print("It is windy today.")
    print("Wear a windbreaker.")
else:
    needs_windbreaker="no"
    print("It is not windy.")
    print("Windbreaker is not required.")

# Check if there are puddles
has_puddles=input("Are there puddles? (yes/no)")

# Decide whether to wear boots or sneakers
if has_puddles=="yes":
    shoes="boots"
    print("There are puddles today.")
    print("Wear",shoes)
else:
    shoes="sneakers"
    print("There are no puddles today.")
    print("Wear",shoes)

# This message always prints no matter what
print("")
print("Weather report complete!")

# Output
print("===== Weather outfit picker =====")
print("Temperature:",temperature)
print("Outfit Chosen:",outfit)
print("Rain?",is_raining)
print("Windbreaker Needed?",needs_windbreaker)
print("Shoes Chosen:",shoes)
print("=================================")