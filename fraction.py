print("Enter numerator here:")
numn=int(input())
numd=int(input("Enter denominator here:"))

if numn%numd==0:
    print("\n",str(numn),"is divisible by",str(numd))
else:
    print("\n",str(numn),"is not divisible by",str(numd))