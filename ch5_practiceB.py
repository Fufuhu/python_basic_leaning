import math

hankei = 10
menseki = lambda x: x * x * math.pi

print("半径:{} -> 面積:{:.3f}".format(hankei, menseki(hankei)))