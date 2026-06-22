sub1, sub2, sub3, sub4, sub5 = map(int, input("enter marks of 5 subjects: ").split())
total=sub1+sub2+sub3+sub4+sub5
average=total / 5
percentage=(total / 500) * 100
print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)