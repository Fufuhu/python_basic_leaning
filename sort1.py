lst1 = ["fly", "good", "ABC", "Bad", "Woo", "Foo", "and"]
lst2 = sorted(lst1)

print(lst2)

lst3 = sorted(lst1, key=str.upper)
print(lst3)