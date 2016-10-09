end = int(input("最後の数値:"))

sum = 0
counter = 0
while counter <= end:
    sum += counter
    counter += 1


print(str(end) + "までの総和:", sum)