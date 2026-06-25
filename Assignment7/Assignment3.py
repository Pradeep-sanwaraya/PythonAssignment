# 3. Multiplication Table
# A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
# Write a program to print the *multiplication table of a given number up to 10 using loops*.

# Input: n = 6
# Output:
# 6 x 1 = 6
# 6 x 2 = 12
# ...
# 6 x 10 = 60
# num=int(input("enter any number"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

num=int(input("enter any number"))
i=0
while i<10:
    i=i+1
    print(num,"x",i,"=",num*i)