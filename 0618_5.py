def args_test(*args):
    return sum(args)

print(args_test(1, 1, 1))
print(args_test(2))
print(args_test(2, 2, 3, 9))