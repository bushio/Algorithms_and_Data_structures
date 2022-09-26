# coding: utf-8

# Frog 問題を「緩和」を意識した動的計画法で解く
INF = 2**60

# c はaとbを格納したリスト (python ではポインタ渡しが不可なため)
def chmin(c: list):
    if (c[0] > c[1]):
        c[0] = c[1]


if __name__ == "__main__":
    # 入力
    N = int(input())
    h = [None] * N
    for i in range(N):
        h[i] = int(input())
    
    # 初期化　（最小化問題なのでINFに初期化)
    dp = [INF] * N

    # 初期条件
    dp[0] = 0
    
    c = [] 
    # ループ
    for i in range(1, N):
        c = [dp[i], dp[i - 1] + abs(h[i] - h[i -1])]
        chmin(c)
        dp[i] = c[0]
        if i > 1:
            c = [dp[i], dp[i - 2] + abs(h[i] - h[i -2])]
            chmin(c)
            dp[i] = c[0]
    # 答え
    print(dp[N-1])