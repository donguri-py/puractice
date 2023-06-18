n = list(map(int, input().split()))
#n1とn2で値を振り分ける
n1 = n[0] #3
n2 = n[-1] #5

for i in range(1, n1 + 1):
    if i == n1:
        print(i)
    else:
        print(i, end=" ")

for i in range(1, n2 + 1):
    if i == n2:
        print(i)
    else:
        print(i, end=" ")


