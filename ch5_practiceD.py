def gen_list(lst):
    gen = []
    for s in lst:
        gen.append(s.upper())
    return gen
        
lst = ["python", "C", "java", "basic", "swift"]
gen = gen_list(lst)
for s in gen:
    print(s)