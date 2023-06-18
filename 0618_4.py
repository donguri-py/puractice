n = input().split()
n2 = int(n[0])
m = int(n[1])

for i in range(1, n2 + 1):
    if i == n2:
        print(i)
    else:
        print(i, end=" ")

for i in range(1, m + 1):
    if i == m:
        print(i)
    else:
        print(i, end=" ")