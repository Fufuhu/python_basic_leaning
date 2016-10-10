
seasons = {"春", "夏", "夏", "秋", "秋", "冬"}

print("{}".format(str(seasons)))

for s in seasons:
    print(s)

lst = {10, 1, 3, 3, 5, 9, 8, 10}
print(str(lst))

lst.add(12)
print("add(12):" + str(lst))

lst.remove(10)
print("remove(10):" + str(lst))

words1 = {"空", "海", "川", "地球"}
words2 = {"山", "海", "空", "空気"}

print("| :" + str(words1 | words2))
print("& :" + str(words1 & words2))
print("- :" + str(words1 - words2))
print("^ :" + str(words1 ^ words2))