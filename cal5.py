from calendar import TextCalendar

year = int(input("年:"))
month = int(input("月:"))

cal = TextCalendar(6)
cal_str = cal.formatmonth(year, month)
print(cal_str)