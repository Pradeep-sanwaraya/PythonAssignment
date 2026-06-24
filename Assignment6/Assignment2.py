#2. College Result Processing System


#A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

#* 90 and above → Grade A
#* 75 to 89 → Grade B
#* 60 to 74 → Grade C
#* 50 to 59 → Grade D
#* Below 50 → Fail

#Write a Python program to display the grade of a student.

#Input:
#Enter marks: 67

#Output:
#Grade: C
grade=int(input("enter your marks"))
if grade>=90:
	print("grade A")
elif grade>=75 and grade<=89:
	print("Grade B")
elif grade>=60 and grade<=74:
	print("Grade c")
elif grade>=50 and grade<=59:
	print("Grade d")
elif grade<50:
	print("fail")
else:
	print("plz enter number upto 100 only")