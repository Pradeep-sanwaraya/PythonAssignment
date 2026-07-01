
# Write a program to:


# - Read withdrawal amount

# - Count how many ₹100 notes needed using loop


# Input:

# 700


# Output:

# Notes = 7

amount=int(input("enter any number"))
note=0
while amount>0:
    if amount>=100:
        amount=amount-100
        note=note+1
print(note)
