class ContextM:
    def __enter__(self):
        print("第一弾")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("最終段階")

    def output(self):
        print("第三弾")

with ContextM() as cm:
    print("第二弾")
    cm.output()