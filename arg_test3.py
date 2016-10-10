def test2(lst):
    print("lst:{}".format(id(lst)))
    lst[0] = 0
    lst.append(100)
    print("lst: {}".format(id(lst)))

l = [1, 2, 3]
test2(l)
print(l)