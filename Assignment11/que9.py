num=int(input("Enter any number: "))
temp=num
even=0
odd=0
while temp>0:
    digit=temp%10
    if digit%2==0:
        even=even+1
    else:
        odd=odd+1
    temp=temp//10
print("Even Count =",even)
print("Odd Count =",odd)
diff=even-odd
if diff<0:
    diff=-diff
print("Difference =",diff)
count=0
for i in range(1,diff+1):
    if diff%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Not Prime")