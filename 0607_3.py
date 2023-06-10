try:
    num = 10 / 0
    print(f"除算の結果は {} になります")
except ArithmeticError as e:
    print(f" Exception class: {type(e)}")
    print(f" Exceptions occurred: {e}")