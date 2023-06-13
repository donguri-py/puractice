import itertools
for value, group in itertools.groupby("aaabbcdddaabb"):
    print(f"{value}: {list(group)}")