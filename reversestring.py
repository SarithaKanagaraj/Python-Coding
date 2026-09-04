# Begin
string=input("Enter your string here:")

# Process
string2=('')

for i in string:
    string2=i+string2

print("\nOriginal String:",string)
print("\nReverse String:",string2)