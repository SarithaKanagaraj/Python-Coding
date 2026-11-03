low_price_item=medium_price_item=high_price_item=0
customers_served=0
total_sales=0
billing=True

while billing:
    name=input("What is your name?")
    item_count=int(input("Enter the number of items you are buying:"))
    if item_count<=0:
        print("Invalid amount!")
        continue
    customer_total=0
    item_number=1
    #Part 5
    while item_number<=item_count:
        item_name=input("Enter the item name:")
        price=int(input("Enter the price here:"))
        quantity=int(input(f"How many {item_name}s are you buying?"))
        if price<=0 or quantity<=0:
            print("Invalid input!")
            continue
        item_total=price*quantity
        print(f"{item_name}:",item_total)
        customer_total+=item_total
        if quantity<=50:
            low_price_item+=1
        elif quantity>50 and quantity<=100:
            medium_price_item+=1
        else:
            high_price_item+=1
        item_number+=1

    customers_served+=1
    total_sales+=customer_total
    next_customer=input("Next customer?(yes/no)")
    if next_customer=="yes":
        continue
    else:
        billing=False

for i in range(0,3):
    for j in range(1,i+1):
        print("*",end="")
print("\nCustomers Served:",customers_served)
print("Total Sales:",total_sales)