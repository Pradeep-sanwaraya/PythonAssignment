# 6.
# Next Prime Cabin Number Generator
# A luxury hotel gives only prime numbered cabins to VIP guests.
# Manager enters the last allotted cabin number.
# System must find the next available prime cabin number.
# Write a program using loops.
# Input:
# 24
# Output:
# Next Prime Cabin = 29
num=int(input("enter your number"))
while True:
    count=0
    num=num+1
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("next cabin prime number is ", num)
        break
