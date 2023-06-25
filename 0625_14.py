names = ["taro", "jiro", "saburo"]
ages = [i for i in range(10, 21, 5)]

for name, age in zip(names, ages):
    print(name, age)