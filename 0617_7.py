# coding: utf-8
# 西暦を令和年に変換
import random
ad_year = random.randint(2019, 2099) #西暦年
print("西暦" + str(ad_year) + "年は", end = "")

# 令和年を計算
era_year = 2019
# 令和年を出力
print("令和" + str(ad_year - era_year + 1) + "年です")
