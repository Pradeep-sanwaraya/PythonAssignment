# 14. Online Course Fee System

# An online platform offers courses with fixed fees:

# * Programming → ₹5000
# * Design → ₹4000
# * Marketing → ₹3000
#   Discount is applied based on user type:
# * Student → 20% discount
# * Working Professional → 10% discount
# * Others → No discount

# Write a Python program to calculate final course fee.

# Input:
# Enter course category: Programming
# Enter user type: Student

# Output:
# Final Course Fee: ₹4000

course=input("enter your course")
user=input("enter your user type")
if course=="programming" and user=="student":
    print("final course fees",5000-(5000*20/100))
elif course=="design" and user=="student":
    print("final course fees",4000-(4000*20/100))
elif course=="marketing" and user=="student":
    print("final course fees",3000-(3000*20/100))
elif course=="programming" and user=="working professional":
    print("final course fees",5000-(5000*10/100))
elif course=="design" and user=="working professional":
    print("final course fees",4000-(4000*10/100))
elif course=="marketing" and user=="working professional":
    print("final course fees",3000-(3000*10/100))
elif course=="programming":
    print("final course fees",5000)
elif course=="design":
    print("final course fees",4000)
else:
    print("final course fees",3000)