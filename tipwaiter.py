def total_calc(total_bill,tip_perc):
    total=total_bill*(1+0.01*tip_perc)
    total=round(total,2)
    print("Total bill =:",total)

total_calc(150,20)