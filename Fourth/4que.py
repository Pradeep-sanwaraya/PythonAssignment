speed=int(input("enter speed: "))
hours,minutes=map(int, input("enter hours and minutes: ").split())
totaltime=hours+(minutes/60)
distance=speed*totaltime
print("TotalTime=",totaltime)
print("Distance=",distance)