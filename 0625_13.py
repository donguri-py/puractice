import copy

l = [[j for j in range(1, 4)] for i in range(1, 4)]
l2 = l.copy()
l3 = copy.deepcopy(l)
print(l)
# print(l2)
print(l3)

# l2[0][0] = 99
l3[0][0] = 88

print(l)
# print(l2)
print(l3)