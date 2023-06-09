def search_x(x, y):
    for i in range(0, len(x), 1):
        if x[i] == y:
            print("見つかりました。添字 :", i)
            break

x = [61, 15, 82, 77, 21, 32, 53]
y = 82

search_x(x, y)