marks=int(input("Enter marks: "))
income=int(input("Enter family income: "))
category=input("Enter category: ")

if marks>=85:
    if income<=300000:
        if category!="general":
            print("Full Scholarship")
        else:
            print("75% Scholarship")
    else:
        print("50% Scholarship")
elif marks>=70 and marks<=84:
    if income<=200000:
        print("50% Scholarship")
    else:
        print("25% Scholarship")
else:
    print("No Scholarship")