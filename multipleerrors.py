try:
    number1=int(input("Enter the first number:"))
    number2=int(input("Enter the second number:"))
    result=number1/number2
    print("Result is",result)
except ZeroDivisionError:
    print("Division by zero is error!")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("Wrong input!")
else:
    print("No exceptions")
finally:
    print("This will print no matter what.")