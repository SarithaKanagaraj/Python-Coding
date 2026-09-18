# Ask for input
print("Right triangle pattern using asterisks(*)")
n=int(input("Enter the number of rows:"))

# Outer loop
for i in range(n):

    #Inner loop
    for j in range(i+1):
        print("* ",end="")
    print()