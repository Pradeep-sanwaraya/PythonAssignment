# 1. Triple Operation Prime Verification System


# A cybersecurity company generates a security score from entered access code.


# Write a program to:


# - Find sum of digits of the number

# - Reverse the number

# - Find absolute difference between original number and reverse

# - Add digit sum and difference

# - Check whether final result is Prime or Not Prime


# Input:

# 4215


# Output:

# Sum of Digits = 12

# Reverse = 5124

# Difference = 909

# Final Result = 921

# Not Prime
num=int(input("engter ANY NUMBER"))
res=0
temp=num
og=num
while num>0:
    rev=num%10
    res=res+rev
    num=num//10
print("sum =",res)
#reverse
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
difference=reverse-og
final=difference+res
print("Reverse=",reverse)
print("difference=",difference)
print("final=",final)

count=0
for i in range(1,final+1):
    if final%i==0:
        count=count+1
if count==2:
    print("prime number ")
else:
    print("not a prime no")


