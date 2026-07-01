# 5.Number Stability Analyzer
# A science lab studies whether digits are in increasing order.
# Write a program using for-else loop:
# - If every next digit is greater than previous print Stable Number
# - Else Unstable Number
# Input:
# 12359
# Output:
# Stable Number
num=int(input("Enter number: "))
prev=10

while num>0:
    r=num%10
    if r>=prev:
        print("Unstable Number")
        break
    prev=r
    num=num//10
else:
    print("Stable Number")