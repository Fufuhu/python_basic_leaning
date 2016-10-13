weekdays = [
    "月曜日\n",
    "火曜日\n",
    "水曜日\n",
    "木曜日\n",
    "金曜日\n",
    "土曜日\n",
    "日曜日\n"
]

with open("days.txt", "w", encoding="utf_8") as f:
    f.writelines(weekdays)
f.close()

f = open("days.txt", "r", encoding="utf_8")
for i, line in enumerate(f):
    print("{:4d}:{}".format(i, line).rstrip("\n"))
f.close()