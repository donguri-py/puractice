
n = list(input())
l = []
for i in range(len(n)):
    l.append(n.pop())
# print(l)
l2 = []
x = 1
for i in range(len(l)):
    if x == len(l):
        l2.append(l[i])
    elif x % 3 == 0:
        l2.append(l[i])
        l2.append(",")
        x += 1
    else:
        l2.append(l[i])
        x += 1
# print(l2)
l3 = []
for i in range(len(l2)):
    l3.append(l2.pop())
# print(l3)
for i in range(len(l3)):
    print(l3[i], end="")