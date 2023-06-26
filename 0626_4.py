a, b = map(int, input().split())
def output(a, b):
    return a // b

def output2(a, b):
    return a % b

def output3(a, b):
    c = a / b
    return "{:.5f}".format(c)

print(output(a, b), output2(a, b), output3(a, b))


