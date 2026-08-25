a=int(input("Enter value here:"))
b=int(input("Enter value here:"))
c=int(input("Enter value here:"))

avg=(a+b+c)/3
print("Average = ",avg)

if avg>a and avg>b and avg>c:
    print("%d is greater than %d, %d, %d" %(avg,a,b,c))
elif avg>a and avg>b:
    print("%d is greater than %d, %d" %(avg,a,b))
elif avg>a and avg>c:
    print("%d is greater than %d, %d" %(avg,a,c))
elif avg>b and avg>c:
    print("%d is greater than %d, %d" %(avg,b,c))
elif avg>a:
    print("%d is greater than %d" %(avg,a))
elif avg>b:
    print("%d is greater than %d" %(avg,b))
elif avg>c:
    print("%d is greater than %d" %(avg,c))
else:
    print("Invalid Input")