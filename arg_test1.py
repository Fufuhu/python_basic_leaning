def test1(num):
    print("num:{}".format(id(num)))
    num += 10
    print("num:{}".format(id(num)))
    
    
n = 3
test1(n)
print(n)