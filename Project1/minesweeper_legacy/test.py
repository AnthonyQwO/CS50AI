ls = [1, 2, 3, 3]
for i, a in enumerate(ls):
    for j, b in enumerate(ls):
        if i != j and a == b:
            ls.remove(a)
print(ls)