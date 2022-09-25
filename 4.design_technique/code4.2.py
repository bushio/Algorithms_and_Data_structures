# coding: utf-8
# 再帰関数
def func(N):
    # 再帰関数を呼び出したことを報告する
    print("func({}) を呼び出しました".format(N))
    if (N == 0):
         return 0
    # 再帰的に答えを求めて出力する
    result = N + func(N - 1)
    print("{} までの和 = {}".format(N, result))
    return result

if __name__ == "__main__":
    func(5)