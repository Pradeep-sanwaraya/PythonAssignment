# 5. Next Prime ID Generator – Smart Version

# A company gives prime numbered employee IDs to premium staff.

# Manager enters current ID.
# System must:

# - Find next prime number after current ID
# - Find difference between current ID and next prime

# Write a program using loops.

# Input:
# 20

# Output:
# Next Prime ID = 23
# Gap = 3
num=int(input("enter any number"))
current=num
while True:
    num=num+1
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    gap=num-current
    if count==2:
        print(f"next prime number{num}gap is {gap} ")
        break