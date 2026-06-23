# 10. Online Exam System
#     System evaluates exam conditions:

# * If marks ≥ 40 → Pass
# * If attendance ≥ 75 → Eligible for certificate
marks=int(input("enter your marks"))
attendance=int(input("enter your attendance"))
if marks>=40:
    print("pass")
if attendance>=75:
    print("Eligible for certificate")