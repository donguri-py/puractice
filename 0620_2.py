n = int(input())

m = [0] * n
values = input().split()
for i in range(n):
    m[i] = int(values[i])

for i in range(n):
    for j in range(1, m[i] + 1):
        if j == m[i]:
            print(j)
        else:
            print(j, end=" ")