lst = ["春", "夏"] + ["秋", "冬"]
print(str(lst))

# リストの繰り返し
lst2 = ["春", "夏"] * 4
print(str(lst2))

# スライスで切り出し num[頭:末尾+1]
num = ["zero", "one", "two", "three", "four", "five", "six"]
print(str(num[2:5]))

# ステップ単位でみる num[::ステップ数]
print(str(num[::2]))

# splitによる区切り
pref = "東京,大阪,名古屋,京都,青森"
lst_str = pref.split(",")
print(str(lst_str))
print(lst_str[2])

# 要素の有無の確認
weekdays = ["日", "月", "火", "水", "木", "金", "土"]
print(str("月" in weekdays))

# indexの取扱い方
words = ["Apple", "Banana", "Curve", "Defence", "Eclipse"]
word = input("文字列:")
try:
    index = words.index(word)
    print("{}のインデックスは{}です。".format(word, index))
except ValueError:
    print("{}は見つかりません".format(word))


# リストの要素へのアクセス
names = ["山田", "井上", "太田", "田中"]
print("変更前:" + str(names))
names[1] = "江藤"
print("変更後:" + str(names))

# リストへの要素追加
print("追加前:" + str(names))
names.append("伊藤")
print("追加後:" + str(names))

# リスト内へのリストの追加
seasons = []
seasons.append("春")
seasons.append(["夏", "秋", "冬"])
print(str(seasons))

# 要素の削除
names = ["山田", "井上", "太田", "田中", "山田"]
names.remove("山田")
print("removedによる削除後:"+str(names))
del names[len(names) - 1]
print("delによる削除後:"+str(names))

## スライスによる削除
names = ["山田", "井上", "太田", "田中", "山田"]
del names[1:4]
print("スライスによる削除後:" + str(names))

# 逆順にする
names = ["山田", "井上", "太田", "田中"] 
names.reverse()
print("reverseによる逆順への変更後:"+ str(names))

# リスト要素の各種数値を得る
nums = [-1, 9, 4, 10]
print("最大:" + str(max(nums)))
print("最小:" + str(min(nums)))
print("合計:" + str(sum(nums)))

# ソートする
nums.sort()
print("昇順ソート(sort()):" + str(nums))
nums.sort(reverse=True)
print("逆順ソート(sort(reverse=True)):" + str(nums))

# sorted
nums_sorted = sorted(nums)
print("sortedの結果:" + str(nums_sorted))
