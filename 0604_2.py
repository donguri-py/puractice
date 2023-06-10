
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

print(n)
print(l)

l2 = []
l3 = []
for i in range(n):
    l2 = []
    for j in range(l[i][0],l[i][1]+1):
        l2.append(j)
    l3.append(l2)
print(l3)

x = []
print(type(x))

for i in range(n):
    x = set(x) & set(l3[i])

print(x)