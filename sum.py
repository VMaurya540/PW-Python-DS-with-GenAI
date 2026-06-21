a = [1,2,3,4,2,3,4,6,7]
b = []
for i in a:
    if i not in b:
        b.append(i)

print(b)