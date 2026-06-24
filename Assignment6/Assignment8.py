
# A weather monitoring system classifies the weather condition based on temperature:

# * Below 0°C → Freezing
# * 0°C to 20°C → Cold
# * 21°C to 35°C → Warm
# * Above 35°C → Hot

# Write a Python program to classify the weather.

# Input:
# Enter temperature: 38

# Output:
# Weather Condition: Hot
temp=int(input("enter your temperature"))
if temp<=0:
    print("freezing")
elif temp<=20:
    print("cold")
elif temp<=35:
    print("warm")
else:
    print("hot")
    