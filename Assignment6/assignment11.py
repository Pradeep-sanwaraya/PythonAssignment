# 11. Railway Ticket Fare System


# A railway system calculates ticket fare based on distance and travel class:

# * Distance ≤100 km:
#   Sleeper → ₹100, AC → ₹200
# * Distance 101–500 km:
#   Sleeper → ₹300, AC → ₹600
# * Distance >500 km:
#   Sleeper → ₹500, AC → ₹1000

# Write a Python program to calculate ticket fare.

# Input:
# Enter distance: 350
# Enter class: AC

# Output:
# Total Fare: ₹600
distance=int(input("enter your distance"))
class=input("enter your class")
if distance<=100:
    if class=="sleeper":
        print("total fare",100)
    else:
        print("total fare",200)
elif distance<=500:
    if class=="sleeper":
        print("total fare",300)
    else:
        print("total fare",600)
else:
    if class=="sleeper":
        print("total fare",500)
    else:
        print("total fare",1000)