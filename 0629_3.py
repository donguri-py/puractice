n = [1, 2, 3]
print(n)

x, y, z = n
print(x, y, z)

a, b, c = [4, 5, 6]
print(a, b, c)

# タプルは省略可
d, e, f = 7, 8, 9
print(d, e, f)

g, h, i = ["python", "C++", "ruby"]
print(g, h, i)

j, k, _ = (10, 20, 30)
print(j, k)
print(_)

# *を変数の前につける事で複数の要素をまとめる事ができる
o, p, *temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(o, p, temp)

q, *temp2, r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(q, temp2, r)

# *を使えば要素数が足りなくても出力できる
aa, bb, *temp3 = (100, 1000)
print(aa, bb, temp3)

# ネスト構造でもアンパックできる
cc, dd, ee = [1, 2, [3, 4, 5]]
print(cc)
print(dd)
print(ee)