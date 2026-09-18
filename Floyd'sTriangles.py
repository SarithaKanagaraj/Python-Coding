# ask for input
rows=int(input("Enter the number of rows:"))
number=1

# outer loop
for i in range(1,rows+1):
    # inner loop
    for j in range(1,i+1):
        #result
        print(number,end='  ')
        number=number+1
    print()