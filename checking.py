from datetime import date

today = date.today()
print(today)
d2 = today.strftime("%Y")
d1 = today.strftime("-%m-%d")
lastyear=str(int(d2)-1)+d1
print(lastyear)
# print("d1 =", str(int(d2)-1)+d1)