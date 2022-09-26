# coding: utf-8

# Frog 問題を「メモ化再帰」で解く


# c はaとbを格納したリスト (python ではポインタ渡しが不可なため)
def chmin(c: list):
    if (c[0] > c[1]):
        c[0] = c[1]

INF = 2**60 # 十分大きい値とする(ここでは 2^60)

h = [None]
dp = [None]
# rec(i): 足場 0 から足場 i までいたるまでの最小コスト
def rec(i):
    # DP の値が更新されていたらそのままリターン
    if dp[i] < INF:
        return dp[i]

    # ベースケース: 足場 0 のコストは 0
    if i == 0:
        return 0

    # 答えを格納する変数を INF に初期化する
    res = INF

    # 足場 i - 1 から来た場合
    c = [res, rec(i-1) + abs(h[i] - h[i - 1]) ]
    chmin(c)
    res = c[0]

    # 足場 i - 2 から来た場合
    if i > 1:
        c = [res, rec(i-2) + abs(h[i] - h[i - 2]) ]
        chmin(c)
        res = c[0]

    # 答えを返す
    dp[i] = res
    return dp[i]

if __name__ == "__main__":
    # 入力受取り
    N = int(input())
    h = [None] * N
    for i in range(N):
        h[i] = int(input())
    
    # 初期化 (最小化問題なので INF に初期化)
    dp = [INF] * N

    # 答え
    print (rec(N - 1))