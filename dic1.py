
dic = {
    "日" : "Sun",
    "月" : "Mon",
    "火" : "Tue",
    "水" : "Wed",
    "木" : "Thu",
    "金" : "Fri",
    "土" : "Sat"
}

key = input("キーを入力してください:")
if key in dic:
    print('キー"{}"が見つかったので削除します'.format(key))
    del dic[key]
    print(dic)
else:
    print('キー"{}"が見つかりませんでした'.format(key))