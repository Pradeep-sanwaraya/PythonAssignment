# 4. Strong Number Checker

# A digital lock opens only for strong numbers.

# A strong number is a number whose sum of factorial of digits equals the number.

# Example:
# 145 = 1! + 4! + 5!

# Write a program using loops to check strong number.

# Input:
# 145

# Output:
# Strong Number
num=int(input("Enter a number: "))
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if temp==sum:
    print("Strong Number")
else:
    print("Not Strong Number")