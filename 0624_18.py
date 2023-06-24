def judge(a, b):
    if a == b:
        return "a == b"
    elif a < b:
        return "a < b"
    else:
        return "a > b"

a, b = map(int, input().split())
print(judge(a, b))
