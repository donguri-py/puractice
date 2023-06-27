def db_test(*args):
    return sum(args)

print(db_test(1, 2, 3, 4, 5))

#　デバッグポイントを設置
import pdb;pdb.set_trace()

print(db_test(6, 7, 8, 9, 10))