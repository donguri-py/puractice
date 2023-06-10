
n = list(input())
l = []
for i in range(len(n)):
    l.append(int(n[i]))

print(l)

for i in range(len(n)):
    if i != 0 and (i + 1) % 3 == 0:
        print(l[i], end=",")
    else:
        print(l[i], end="")