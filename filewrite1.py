with open("out.txt", "w", encoding="utf_8") as f:
    f.write("こんにちは")
    f.write("Pythonの世界へようこそ")
    f.write(str(2016))
    f.write("年\n")

f.close()

f = open("sample.txt", "r", encoding="utf_8")

for i, line in enumerate(f):
    print("{:4d}: {}".format(i + 1, line.rstrip("\n")))    

f.close()