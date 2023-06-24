def judge(a, b, c):
    if a < b < c:
        return "Yes"
    else:
        return "No"

a, b, c = map(int, input().split())
print(judge(a, b, c))
