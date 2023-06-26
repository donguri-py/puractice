a, b, c = map(int, input().split())
l = [i for i in range(a, b + 1)]
l2 = []
for i in l:
    if c % i == 0:
        l2.append(i)
print(len(l2))