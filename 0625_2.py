l = list(map(int, input().split()))
x = sorted(l)

for i in range(3):
    if i == 2:
        print(x[i])
    else:
        print(x[i], end=" ")