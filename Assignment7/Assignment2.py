# 2. Factorial of a Number
# In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
# Write a program to calculate the *factorial of a given number using loops*.

# Input: n = 5
# Output: Total Ways = 120


# num=int(input("enter any number"))
# Fact=1
# i=1
# while i<=num:
#        Fact=Fact*i
        
#        i=i+1
# print(Fact)
    

num=int(input("enter any number"))
Fact=1
i=1
for i in range(1,num+1):
       Fact=Fact*i
print(Fact)