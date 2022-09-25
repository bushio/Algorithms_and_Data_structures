# coding: utf-8
# フィボナッチ数列を求める再帰関数をメモ化
def fibo(N):

    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1

    # メモをチェック(すでの計算ずみならば答えをリターンする)
    if memo[N] != -1:
        return memo[N]

    # 答えをメモ化しながら,再帰呼出し
    
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]


if __name__ == "__main__":
    # メモ化用配列を　-1 で初期化する
    global memo 
    memo = [-1] * 50

    # fibo(49) をよびだす
    fibo(49)

    # memo[0], ..., memo[49] に答えが格納されている
    for N in range(2, 50):
        print("{} 項目 = {}".format(N, memo[N]))

