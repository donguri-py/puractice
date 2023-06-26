import itertools
for value, group in itertools.groupby("XXXXXXXAXXXXXYYYYYYYYYYFYYYZZZZZZGZZZZZZZ"):
    print(f"{value}: {list(group)}")