l = []
for i in range(10001):
    x = int(input())
    if x == 0:
        break
    else:
        l.append(x)
num = 1
for i in range(len(l)):
    print(f"Case {num}: {l[i]}")
    num += 1