monthlys,workingday,workingperhour=map(int, input("enter your salary working day working per hour").split())
perday=monthlys/workingday
perhour=perday/workingday
print("salary per day",perday)
print("salary per hour",perhour)