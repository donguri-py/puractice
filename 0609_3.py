l = [2, 5, 1, 4, 6, 3]
l2 = []
while l != []:
    l2.append(min(l))
    l.remove(min(l))

print(l2)