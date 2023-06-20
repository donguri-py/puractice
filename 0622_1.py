n = list(map(int, input().split()))
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

for i in range(n[1]):
    for j in range(l2[i]):
        if l2[i]-1 == j:
            print(l1.pop(0))

        else:
            print(l1.pop(0), end=" ")
