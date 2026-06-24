# 15. Smart Parking System

# A smart parking system charges based on vehicle type and parking duration:

# * Bike → ₹10/hour
# * Car → ₹20/hour
# * Bus → ₹50/hour
#   If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

# Write a Python program to calculate total parking fee.

# Input:
# Enter vehicle type: Car
# Enter hours parked: 6

# Output:
# Total Parking Fee: ₹220

vehicle=input("enter your vehicle type")
hours=int(input("enter your hours"))
if vehicle=="bike":
    print("total parking fee",hours*10) 
elif vehicle=="car":
    print("total parking fee",hours*20)
elif vehicle=="bus":
    print("total parking fee",hours*50)
else:
    print("total parking fee",hours*100)