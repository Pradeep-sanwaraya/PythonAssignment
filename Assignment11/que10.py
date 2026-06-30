
# 10.Zero Count Prime Scanner

# A banking system checks account numbers.

# Write a program to:

# - Count zero digits
# - Find sum of digits
# - Add zero count and sum
# - Multiply by smallest digit
# - Check whether final result is Prime or Not

# Input:
# 908406

# Output:
# Zero Count = 2
# Sum = 27
# Smallest Digit = 0
# Final Result = 0
# Not Prime
num=int(input("Enter any number: "))
temp=num
zero=0
sum=0
small=9
while temp>0:
    digit=temp%10
    if digit==0:
        zero=zero+1
    sum=sum+digit
    if digit<small:
        small=digit
    temp=temp//10
print("Zero Count =",zero)
print("Sum =",sum)
print("Smallest Digit =",small)
result=(zero+sum)*small
print("Final Result =",result)
count=0
for i in range(1,result+1):
    if result%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Not Prime")