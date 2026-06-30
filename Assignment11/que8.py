
# 8. Largest Smallest Sum Prime Checker

# A number analyzer finds largest and smallest digit.

# Write a program to:

# - Find largest digit
# - Find smallest digit
# - Find sum of both
# - Check whether sum is Prime or Not

# Input:
# 57294

# Output:
# Largest = 9
# Smallest = 2
# Sum = 11
# Prime
num=int(input("Enter any number: "))

temp=num

large=0
small=9

while temp>0:
    digit=temp%10

    if digit>large:
        large=digit

    if digit<small:
        small=digit

    temp=temp//10

print("Largest =",large)
print("Smallest =",small)

sum=large+small
print("Sum =",sum)

count=0

for i in range(1,sum+1):
    if sum%i==0:
        count=count+1

if count==2:
    print("Prime")
else:
    print("Not Prime")