
# 7.
#  Prime Sum Lucky Number

# A lottery app checks if sum of digits is prime.

# Write a program to:

# - Find sum of digits
# - If prime print Lucky Number
# - Else Normal Number

# Input:
# 4528

# Output:
# Sum = 19
# Lucky Number
num=int(input("Enter any number: "))

temp=num
sum=0

while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10

print("Sum =",sum)

count=0

for i in range(1,sum+1):
    if sum%i==0:
        count=count+1

if count==2:
    print("Lucky Number")
else:
    print("Normal Number")