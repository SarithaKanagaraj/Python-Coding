print("Enter Marks Obtained in 5 Subjects:")

mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

total=mark1+mark2+mark3+mark4+mark5
avg=int(total/5)

validRange=range(0,101)

if avg not in validRange:
    print("Invalid Input!")
elif avg in range(91,101):
    print("Grade is A1")
elif avg in range(81,91):
    print("Grade is A2")
elif avg in range(71,81):
    print("Grade is B1")
elif avg in range(61,71):
    print("Grade is B2")
elif avg in range(51,61):
    print("Grade is C1")
elif avg in range(41,51):
    print("Grade is C2")