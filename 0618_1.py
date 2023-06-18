n = int(input())
m = n // 2
# n を1/2にしてmに代入する

for i in range(1, m + 1):
    if i == m:
        print(i)
    else:
        print(i ,end=" ")

for i in range(m + 1, n + 1):
    if i == n:
        print(i)
    else:
        print(i, end=" ")

