# 7. Duck Number Checker

# A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

# A duck number is a number that contains at least one zero but does not start with zero.

# Example:
# 1023

# Write a program using loops to check whether the entered number is a Duck number.

# Input:
# 1023

# Output:
# Duck Number
num=int(input("Enter a number: "))
flag=0
while num>0:
    digit=num%10
    if digit==0:
        flag=1
        break
    num=num//10
if flag==1:
    print("Duck Number")
else:
    print("Not Duck Number")