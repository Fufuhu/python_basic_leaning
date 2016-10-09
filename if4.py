age = int(input("年齢を入力:"))

if age <= 3:
    print("無料")
elif age < 13:
    print("200円です")
elif age < 65:
    print("400円です")
else:
    print("無料です")    