import sys


try:
    heisei = int(input("平成の年を入力:"))
except ValueError:
    print("数字を入力してください")
    sys.exit()

print("平成{}年は西暦{}年です".format(heisei, heisei + 1988))