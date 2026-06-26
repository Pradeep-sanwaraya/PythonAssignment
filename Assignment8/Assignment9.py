# 9. Neon Number LED Unlock Game
# You're programming a new LED display game. The game level unlocks only when a neon number is entered.

# A neon number is a number where the sum of the digits of its square is equal to the number itself.
# Example: 9 → 9² = 81 → 8 + 1 = 9

# Accept a number from the player.
# Check whether it is a neon number using loops.

# If true, display:
# Glowing Success! You've found the Neon Number!

# Otherwise display:
# Try again! Not quite glowing yet.
num=int(input("enter any number"))
square=num*num
sum=0
temp=num
while square>0:
    d=square%10
    sum=sum+d
    square=square//10
if temp==sum:
    print("number is a neon ",sum)
else:
     print("number is not  a neon ",sum)