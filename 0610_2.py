n = list(input().split())
list_str = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_answer = []
for i in list_str:
    list_answer.append(int(n[0] + i + n[1]))

x = 0
y = 0
for i in list_int[:-1]:
    for j in list_int:
        if (((i * 10) + j) * j) in list_answer:
            x = i
            y = j
            break
        else:
            pass

if x == 0 and y == 0:
    print("No")
else:
    print(x, y)





