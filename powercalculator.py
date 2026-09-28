base=int(input("Enter base here:"))
exponent=int(input("Enter exponent here:"))

result=1
for i in range(1,exponent+1):
    result=result*base
    print("Step", i, ": result =",result)

print("\nAnswer:", base,"to the power of",exponent,"=",result)