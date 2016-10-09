import sys

try:
    cm = float(input("cmで入力してください:"))
except ValueError:
    print("数値を入力してください")
    sys.exit()

inch_per_cm = 2.54

print("{:.3f} cmは{:.3f} inchです".format(cm, cm/ inch_per_cm))