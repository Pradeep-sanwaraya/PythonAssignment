totalsecond=int(input("enter seconds"))
hours=int(totalsecond/3600)
minute = int((totalsecond % 3600) / 60)
second=totalsecond%60
print(hours,minute,second)
