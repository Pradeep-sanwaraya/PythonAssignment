# 4. Prime Security Code Checker – Advanced

# A high-security lab accepts only prime numbered access codes.

# When a user enters a number, the software must:

# - Check whether number is prime
# - If prime, print next immediate prime number
# - If not prime, print previous immediate prime number

# Write a program using loops only.

# Input:
# 29

# Output:
# Prime Number
# Next Prime = 31
num=int(input("enter any number"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("prime no ")
    next=num

    while True:
        next=next+1
        nextcount=0
        for i in range(1,next+1):
            if next%i==0:
                nextcount=nextcount+1
        if nextcount==2:
            print("next prime number is",next)
            break
else:
    print("Not a Prime Number")

    prev = num

    while True:
        prev = prev - 1
        count = 0

        for i in range(1, prev + 1):
            if prev % i == 0:
                count = count + 1

        if count == 2:
            print("Previous Prime =", prev)
            break
       
                


        
