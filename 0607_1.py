
try:
    num = 10 / 2
    # print(f"除算の結果は {num} になります")
except (ZeroDivisionError, TypeError, NameError) as e:
    print(f" Exceptions class: {type(e)}")
    print(f" Exceptions occurred: {e}")
else:
    print(f"除算の結果は {num} になります")