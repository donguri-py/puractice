a = int(input())
if a > 0:
    print("plus")
else:
    print(a)

b = input()
if b == "hoge":
    print("yes")
else:
    print(b)

c = input()
if len(c) == 10:
    print("ten")
else:
    print(c)

d = input()
if "x" in d:
    print(d.find("x"))
else:
    print("nothing")

e = input()
if len(e) == 5:
    print("five")
else:
    print(e[0])