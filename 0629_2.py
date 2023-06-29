# test_text.txtの内容 "abcdefg"
f = open("test_text.txt", "r", encoding='UTF-8')
data_output = f.read()
print(data_output)
