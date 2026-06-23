# 8. Number Property Checker
#    A system evaluates number properties:

# * If number % 2 == 0 → Even number
# * If number % 5 == 0 → Divisible by 5
# * If number % 7 == 0 → Divisible by 7
num=int(input("enter your number"))
if num%2==0:
    print("Even number")
else:
        print("Odd number")
if num%5==0:
    print("Divisible by 5") 
else:
    print("Not divisible by 5")