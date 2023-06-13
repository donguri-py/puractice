import itertools

it = itertools.chain(["A","B"], "ab", range(3))
for element in it:
    print(element)
