# 2. Multi Stage Prime Lock System


# A smart locker opens only if final derived number is prime.


# Write a program to:


# - Find sum of digits

# - Find product of digits

# - Find difference between product and sum

# - Count digits in difference

# - Add digit count to difference

# - Check whether final result is Prime or Not


# Input:

# 234


# Output:
# Sum = 9
# Product = 24
# Difference = 15
# Digits = 2
# Final Result = 17
# Prime
num=int(input("enter any number"))
temp=num
result=0
while num>0:
    r=num%10
    result=result+r
    num=num//10
print("sum=",result)
#product

num=temp
product=1
while temp>0:
    r=temp%10
    product=product*r
    temp=temp//10
print("product=",product)
diff=product-result
print("diffrence",diff)
ediff=diff
count=0
while diff>0:
    dig=diff%10
    if dig!=0:
        count=count+1
    diff=diff//10
print("digits",count)
add=ediff+count
print("final res=",add)

count=0
for i in range(1,add+1):
    if add%i==0:
        count=count+1
if count==2:
    print("prime number ")
else:
    print("not a prime number")