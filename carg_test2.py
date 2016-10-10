import sys


sum = 0
for i in range(1, len(sys.argv)):
    try:
        sum += float(sys.argv[i])
    except ValueError:
        print("数値を入力してください")
        sys.exit(1)

print("総和:{}".format(sum))