
print("整数の最大値を求める")

x = int(input("xの値"))
y = int(input("yの値"))
z = int(input("zの値"))

maxdata = x
if y > maxdata: maxdata = y
if z > maxdata: maxdata = z

print(f"最大値は{maxdata}である。")
