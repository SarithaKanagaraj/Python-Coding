# Collect a name and club name
name=input("Enter Student Name:")
club=input("Enter Student Club:")

# Collect details
age=11
height=4.2
hobby="soccer"
is_active=True

# Convert into text
age_txt=str(age)
height_txt=str(height)
is_active_txt=str(is_active)

# Slice string into badge
first_three=hobby[0:3]
last_letter=hobby[-1]
badge_code=first_three+last_letter
reverse_badge_code=badge_code[::-1]

# Complete Badge
print("==========================")
print("Name:",name)
print("Club:",club)
print("Age:",age_txt,"|Height:",height_txt,"|Hobby:",hobby)
print("Is Active:",is_active_txt)
print("Badge Code:",reverse_badge_code)
print("==========================")
