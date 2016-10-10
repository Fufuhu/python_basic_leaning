colors = {
    "red" : "赤",
    "green" : "緑",
    "blue" : "青"
}

print(str(colors))

print(str(len(colors)))

print(colors["red"])

colors["yellow"] = "黄"
print(str(colors))

del colors["yellow"]

print("削除後:" + str(colors))

# 存在しないものを削除しようとするとKeyError発生
try:
    del colors["marble"]
except KeyError:
    print("存在しないキーを削除しようとしています。")

