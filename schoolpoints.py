# Teams

Team1=125
Team2=130
Team3=120
Team4=140
Team5=123

# Total and average points
Total=Team1+Team2+Team3+Team4+Team5
Average=Total/5

print("Total points:",Total)
print("Average points per team:",Average)

# How many stars will be accounted for each point
stars_per_point=10
T1star=stars_per_point*Team1
T2star=stars_per_point*Team2
T3star=stars_per_point*Team3
T4star=stars_per_point*Team4
T5star=stars_per_point*Team5
total_stars=T1star+T2star+T3star+T4star+T5star
print("Total Stars:",total_stars)

# How many boxes are needed for 25 stars each
box=25
total_boxes=total_stars//box
print("Total boxes:",total_boxes)

# Calculate the remaining stars
rem=total_stars%box
print("Remaining stars =",rem)

# Compare with last week's stars
last_week=stars_per_point*700
print("Better than last week?",total_stars>last_week)
print("Worse than last week?",total_stars<last_week)
print("As good as last week?",total_stars>=last_week)

# Bonus and subtract missed task

total_stars+=200
print("Total stars after bonus:",total_stars)
total_stars-=500
print("Total stars after missed task:",total_stars)
