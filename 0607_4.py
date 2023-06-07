
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
# print(n)
# print(l)
l2 = []
for i in range(n):
    l2.append(l[i][1:])

for i in range(n):
    print(*l2[i])