totalbill, service, gst = map(int, input("enter total bill service charge and gst: ").split())
num = int(input("enter number of friends: "))
gst = (totalbill * gst) / 100
service = (totalbill * service) / 100
finalbill = totalbill + gst + service
eachperson = finalbill / num
print("Final Bill =", finalbill)
print("Each Person Pays =", eachperson)