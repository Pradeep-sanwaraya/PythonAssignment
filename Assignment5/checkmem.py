# 9. Library Access System
#    A library checks:

# * If membership is active → Entry allowed
# * If books issued < 3 → Can issue more books
membership=int(input("enter your membership active/not"))
books=int(input("enter number of books issued"))
if membership=="active":
    print("Entry allowed")
if books<3: 
    print("Can issue more books")