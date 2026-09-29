# Functions
def greeting_message():
    print("Welcome to the lemonade stand!")
    print("Freshly squeezed lemonade just for you!")

def calculate_price(cups,price):
    total=cups*price
    return total

def calculate_change(amount_paid,rounded_total):
    change=amount_paid-rounded_total
    return change

def thank_you_message(cups):
    if cups>=5:
        return "That's a big order! THank you so much!"
    else:
        return "Thank you for ordering!"


greeting_message()
total_cups=int(input("Enter the number of cups that were sold:"))
price_per_cup=float(input("Enter the price for each cup:"))
total_revenue=calculate_price(total_cups,price_per_cup)
print("Total revenue:",total_revenue)

customer_paid=float(input("How much did you pay?"))

round_total_revenue=round(total_revenue,2)
customer_change_returned=calculate_change(customer_paid,round_total_revenue)
print("Change:",customer_change_returned)

goodbye_message=thank_you_message(total_cups)

print("=====RECEIPT=====")
print("Price per cup:",price_per_cup)
print("Cups sold:",total_cups)
print("Total cost:",total_revenue)
print("Amount paid:",customer_paid)
print("Change due",customer_change_returned)
print(goodbye_message)
print("=================")