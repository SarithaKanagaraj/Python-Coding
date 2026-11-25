
#4 functions 
def add(num1,num2):
    add_result=num1+num2
    return add_result
def subtract(num1,num2):
    subtract_result=num1-num2
    return subtract_result
def multiply(num1,num2):
    multiply_result=num1*num2
    return multiply_result
def divide(num1,num2):
    divide_result=num1//num2
    return divide_result

try:
    num1=num1=float(input("Enter 1st number here:"))
    num2=float(input("Enter 2nd number here:"))
    print("Addition:",add(num1,num2))
    print("Subtraction:",subtract(num1,num2))
    print("Multiplication:",multiply(num1,num2))
    print("Divison:",divide(num1,num2))
except ValueError:
    print("That is not a number! Please enter a valid number!")
except ZeroDivisionError:
    print("That is not divisible by zero!")