n = int(input())
l = [input().split() for _ in range(n)]

l2 = [l[i][1:] for i in range(n)]

for i in range(n):
    for j in range(len(l2[i])):
        if j == len(l2[i]) - 1:
            print(l2[i][j])
        else:
            print(l2[i][j], end=" ")


