year = int(input("西暦:"))

if((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(str(year) + "年はうるう年です")
else: 
    print(str(year) + "年はうるう年ではありません。")