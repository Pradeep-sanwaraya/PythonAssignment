#1. Electricity Department Billing System


#The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based #on slab-wise unit consumption:

#* First 100 units are charged at ₹5 per unit
#* Next 100 units (101–200) are charged at ₹7 per unit
#* Units above 200 are charged at ₹10 per unit


unit=int(input("enter  your monthly unit"))
if unit<=100:
	print(100*5)
elif unit<=200:
	print((100*5)+((unit-100)*7))
else:
	print((100*5)+((unit-100)*7)+((unit-200)*10))