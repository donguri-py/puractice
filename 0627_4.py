import itertools
sorted_text = "".join(sorted("XXXXXXXAXXXXXYYYYYYYYYYFYYYZZZZZZGZZZZZZZ"))
print(sorted_text)

for value, group in itertools.groupby(sorted_text):
    print(f"{value}: {list(group)}")