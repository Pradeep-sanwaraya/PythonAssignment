# 4. E-Learning Course Access System

# An online learning platform grants access based on subscription type, course progress, and test score.

# If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

# Input:
# Subscription = premium
# Progress = 85
# Test Score = 65

# Output:
# Access Status = Retry Test
subscription=input("enter your subscription")
progress=int(input("enter your progress"))
score=int(input("enter your score"))
if subscription=="premium" and progress>=80 and score>=70:
    print("access status=unlock certificate")
elif subscription=="premium" and progress<80:
    print("access status=complete course")
elif subscription=="basic" and progress>=50:
    print("access status=limited access")
else:
    print("access status=deny access")