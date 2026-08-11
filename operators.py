# Harvest for each kg of rice per field
field1=120
field2=85
field3=150
field4=95
field5=110

# Total amount of harvest
total=field1+field2+field3+field4+field5
average=total/5

print("Total Harvest=",total,"kgs")
print("Average Harvest per Field=",average,"kgs")

# Price per kg is 15. calculate total earnings
price_per_kg=15
earnings=total*price_per_kg
print("Total earnings: Rs.",earnings)

# Pack the bags with 25 kgs
bags=total//25
leftover=total%25
print("Total number of bags:",bags)
print("Leftover amount:",leftover)

# Comparing to last year
lastyear=500
print("Better than last year?",total>lastyear)
print("Same as last year?",total==lastyear)
print("Atleast as good?",total>=lastyear)

# A bonus field addds 30 kgs to the total
total+=30
print("After bonus crop:",total,"kgs")

# Subtract 15 kgs as seed reserve for next year
total-=15
print("After reduction:",total,"kgs")

# Final Bag Count
bags=total//25
print("Final bags packed",bags)