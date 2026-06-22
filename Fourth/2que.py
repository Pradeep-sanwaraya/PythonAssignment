mobileprice, downpayment, interest, month = map(int, input("enter mobile price downpayment interest month: ").split())
remaining = mobileprice - downpayment
interest = (remaining * interest) / 100
totalwithinterest = remaining + interest
monthly = totalwithinterest / month
print("Remaining Amount =", remaining)
print("Total with Interest =", totalwithinterest)
print("Monthly EMI =", monthly)