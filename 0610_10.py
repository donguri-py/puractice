n = list(map(int, input().split()))

for i in range(1, n[0] + 1):
    if i == n[0]:
        print(i)
    else:
        print(i, end=" ")
for i in range(1, n[1] + 1):
    if i == n[1]:
        print(i)
    else:
        print(i, end=" ")
