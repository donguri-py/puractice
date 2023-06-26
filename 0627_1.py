def gen():
    print("A")
    yield "X"
    print("B")
    yield "Y"
    print("C")
    yield "Z"

gen_obj = gen()
print(next(gen_obj))
print("ここで関数genの外のprintを実行\ngen内に戻る")

print(next(gen_obj))
print("ここで関数genの外のprintを実行\ngen内に戻る")

print(next(gen_obj))
print("ここで関数genの最後の部分が出力される\n終了")

