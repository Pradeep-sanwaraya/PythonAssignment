

# 7.

#  Alternate Digit Prime Checker


# A math lab adds alternate digits from right side.


# Write a program to:


# - Find sum of alternate digits

# - Check whether sum is Prime or Not


# Input:

# 12345


# Output:

# Alternate Sum = 9

# Not Prime
num = int(input("Enter number: "))
res=0
while num > 0:
    r = num % 10
    num=num//10
    res=res+r

    
    num = num // 10
print(res)
count=0
for i in range(1,res+1):
     if res%i==0:
         count=count+1
if count==2:
     print("Prime")
else:
     print("Not Prime")
