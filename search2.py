str1 = "水金地火木土"
str2 = input("検索文字列を入力:")

index = str1.find(str2)
if index != -1:
    print(str2 +"が見つかりました")
    print("index:", index)
else:
    print(str2 +"は見つかりませんでした")