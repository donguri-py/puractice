l = [i**2 for i in range(10) if i % 2 == 0]
print(l)

print([i**2%10 for i in range(10)])

print({i**2%10 for i in range(10)})

print({i: i**2 for i in range(5)})


