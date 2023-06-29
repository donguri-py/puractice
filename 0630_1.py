def sample_deco(func):
    print("デコレーターテスト")
    return func

@sample_deco
def sample_fun():
    pass

sample_fun()
