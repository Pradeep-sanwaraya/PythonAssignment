

# 8.
# Mirror Difference Transaction Verification System
# A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
#  the security software performs a Mirror Difference Verification Test.
# For every entered transaction ID:

# Reverse the digits of the transaction ID

# Find the absolute difference between the original ID and the reversed ID


# Count the total number of digits in the difference


# Apply the following conditions using if-elif-else:

# If the difference is 0, print Perfect Match


# Else if the difference is divisible by 9, print Verified


# Else print Rejected
num=int(input("Enter number: "))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
diff=abs(num-rev)
count=0
temp=diff
if temp==0:
    count=1
else:
    while temp>0:
        count=count+1
        temp=temp//10
if diff==0:
    print("Perfect Match")
elif diff%9==0:
    print("Verified")
else:
    print("Rejected")
print("Digits =",count)