import itertools
it = itertools.chain(["A", "B"], "ab", range(3))
for i in it:
    print(i)