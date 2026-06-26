
# 10. Student ID Validity Checker (Count Odd Digits)
# A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

# Write a program to count the number of odd digits in a given student ID using loops.

# Input:
# 572943

# Output:
# Odd Digits Count = 3
num=int(input("enter any number"))
count=0
while num>0:
    d=num%10
    if num%2==0:
        count=count+1
    num=num//10
print("number of odd digit is",count)