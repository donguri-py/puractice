n = int(input())
l = []
for i in range(n):
    l.append(list(map(float, input().split())))

for i in range(n):
    l[i][1] = int(l[i][1])

for i in range(n):
    print("{:.{}f}".format(l[i][0],l[i][1]))