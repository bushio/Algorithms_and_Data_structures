# coding: utf-8
# 再帰関数
def func(N):
    print("func({}) を呼び出しました".format(N))
    if (N == 0):
         return 0
    result = N + func(N - 1)
    print("{} までの和 = {}".format(N, result))
    return result

if __name__ == "__main__":
    func(5)