num = int(input("数字:"))

if((num % 3 == 0) or (num % 5 == 0)) and (num >= 100):
    print("100以上かつ、3または5の倍数です")