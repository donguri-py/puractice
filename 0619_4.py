mydict = {"A":1, "B":2, "C":3}

print(mydict.values())

for myvalues in mydict.values():
    print(myvalues)

mylist = list(mydict.values())
print(mylist)