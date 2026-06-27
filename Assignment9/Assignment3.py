
# 6. Banking Fraud Detection System

# A bank monitors transactions based on amount, location, OTP verification, and account age.

# If transaction amount is at least 10000, then check location. If international, 
# then check OTP verification. If verified, allow; otherwise block. If location is domestic,
# then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years,
# allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000,
# then check unusual activity. If yes, flag; 
# otherwise allow.

# Input:
# Transaction Amount = 60000
# Location = domestic
# Account Age = 1

# Output:
# Transaction Status = Flagged
transaction=int(input("enter your transaction amount"))
location=input("enter your location")
otp=input("enter your otp")
accountage=int(input("enter your account age"))
if transaction>=10000:
    if location=="international":
        if otp=="verified":
            print("allow")
        else:
            print("block")
    else:
        if transaction>=50000:
            if accountage>=2:
                print("allow")
            else:
                print("flag")
        else:
            print("allow")
else:
    if otp=="unusual":
        print("flag")
    else:
        print("allow")