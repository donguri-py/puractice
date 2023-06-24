import copy
l = []
for i in range(3001):
    l2 = list(map(int, input().split()))
    if l2[0] == 0:
        break
    else:
        l.append(l2)
print(l)
l3 = copy.deepcopy(l)
print(l3)

for i in range(len(l)):
    l3[i][0] = l[i][1]
    l3[i][1] = l[i][0]


print(l3)
print(l)

