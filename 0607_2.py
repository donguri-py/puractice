f = None
try:
    f = open("python.txt", mode="w")
    f.write(data)
finally:
    if f:
        f.close()
        print("ファイルを閉じました")