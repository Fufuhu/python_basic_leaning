secret = "foo"

while True:
    word = input("秘密の言葉を入力してください:")
    if word == secret:
        print("正解")
        break
    else:
        print("不正解")
        