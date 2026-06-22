runs = int(input("enter runs"))
overs = int(input("enter overs"))
balls = int(input("enter balls"))

totalballs=(overs*6)+balls
totalovers=totalballs/6

runrate=runs/totalovers

print("TotalBalls="totalballs)
print("Run Rate=",runrate)