#3. Income Tax Department System

#The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

#* Up to ₹2,50,000 → No tax
# ₹2,50,001 to ₹5,00,000 → 5% tax
#* ₹5,00,001 to ₹10,00,000 → 20% tax
#* Above ₹10,00,000 → 30% tax
#Write a Python program to calculate the tax amount.
tax=int(input("enter your anuual income"))
if tax<=250000:
	print("no tax")
elif tax<=500000:
	print("5% tax",tax*5/100)
elif tax<=100000:
	print("20% tax",tax*20/100)
else:
	print("30% tax",tax*30/100)
