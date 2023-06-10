list = []
for i in range(10):
    list.append(i**2)
print(list)

list2 = [i**2 for i in range(10)]
print(list2)

list3 = [i for i in range(10)]
print(list3)

list4 = [str(i) for i in list3]
print(list4)