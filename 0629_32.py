n = int(input())
l = []
for i in range(n):
    list_in = list(map(int, input().split()))
    l.append(list_in[1:])

for i in range(n):
    print(*l[i])