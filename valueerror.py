try:
    number=int(input("Enter number here:"))
    print("The number entered is",number)
except ValueError as ex:
    print("Exception",ex)