
# 4.Unique Digit Security Scanner


# A smart locker accepts only numbers whose all digits are unique.


# Write a program using for-else loop to:


# - Check every digit

# - If any repeated digit found reject

# - Else accept

# Input:

# 57294


# Output:

# Valid Unique Code
num=int(input("enter any number"))
for i in range(1,len(str(num))):
    d=str(num%10)
    s=str(num//10)
    if d in s:
        print("repeated digit found")
        break
else:
    print("valid unique code")
    