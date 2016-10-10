lst = [
    100,
    200,
    100,
    200,
    300,
    400,
    90,
    100,
    50
]

# リストから集合を作る
num = {num for num in lst if num > 100}
print(num)