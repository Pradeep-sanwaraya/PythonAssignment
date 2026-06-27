# 10. Smart Restaurant Order Processing System

# A restaurant offers discounts and benefits based on order amount, customer type, and payment method.

# If order amount is at least 2000, then check customer type. If VIP, then check payment method. If online, give free dessert and 20 percent discount; otherwise only free dessert. If not VIP, then check if amount is at least 5000. If yes, give 15 percent discount; otherwise 10 percent discount. If order amount is less than 2000, then check if it is at least 1000. If yes, then if customer is VIP, give 10 percent discount; otherwise 5 percent discount. If below 1000, no offer.

# Input:
# Order Amount = 2500
# Customer Type = VIP
# Payment Method = online

# Output:
# Offer = Free Dessert + 20% Discount
orderamount=int(input("enter your orderamount"))
customer=input("enter your customer")
payment=input("enter your payment")
if orderamount>=2000:   
    if customer=="vip:
        if payment=="online":
            print("free dessert and 20 percent discount")
        else:
            print("free dessert")
    else:
        if orderamount>=5000:
            print("15 percent discount")
        else:
            print("10 percent discount")
else:
    if orderamount>=1000:
        if customer=="vip":
            print("10 percent discount")
        else:
            print("5 percent discount")
    else:
        print("no offer")