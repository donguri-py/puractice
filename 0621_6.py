n = int(input())

for _ in range(n):
    values = input().split()
    x = float(values[0])
    y = int(values[1])

    print("{:.{}f}".format(x, y))