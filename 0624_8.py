def profit(a, b):
    if a < b:
        return "Yes"
    else:
        return "No"

x = profit(int(input()), int(input()))
print(x)