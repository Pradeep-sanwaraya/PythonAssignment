
# 2. Next Prime ID Generator

# A multinational company auto-generates employee IDs in numeric sequence.
#  Due to internal policy, only prime numbered IDs are assigned to new premium employees.

# The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

# Write a program to find the first prime number after n.

# Input:
# 14

# Output:
# Next Prime = 17
num=int(input("enter any number"))
while True:
    num=num+1
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("next prime number ",num)
        break