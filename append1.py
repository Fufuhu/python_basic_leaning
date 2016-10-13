with open("out.txt", "a", encoding="utf_8") as f:
    f.write("さようなら\n")

f.close()

f = open("out.txt", "r", encoding="utf_8")

for i, line in enumerate(f):
    print("{:4d}: {}".format(i + 1, line.rstrip("\n")))    

f.close()