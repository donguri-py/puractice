n = "abcdefg"
print(list(n))

a = "15478256556"
print(list(a))

l1 = [1, 2, 3, 4, 5]
print(l1[::2]) #2つ飛ばし

l2 = [1, 2, 3, 4, 5]
print(l2[::-1]) #リスト反転

x = [1,2,3,4,5]
y = [6,7,8,9,10]

z = x + y
print(z)

x += y

print(x)
x = [1,2,3,4,5]
y = [6,7,8,9,10]

x.extend(y)
print(x)

