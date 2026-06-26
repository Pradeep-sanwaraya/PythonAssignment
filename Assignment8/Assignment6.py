
# 6. Sum of Factors
# A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
# Write a program to find sum of factors using loops.

# Input:
# 6

# Output:
# Sum = 12
# num=int(input("enter any number"))
# i=1
# count=0
# res=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1
#         res=res+i
# print(res)
num=int(input("enter any number"))
i=1
count=0
res=0
while i<=num:
    if num%i==0:
        count=count+1
        res=res+i
    i=i+1    
print(res)