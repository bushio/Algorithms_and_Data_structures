# coding: utf-8

# Frog 問題を「配る遷移形式」で解く
INF = 2**60

# c はaとbを格納したリスト (python ではポインタ渡しが不可なため)
def chmin(c: list):
    if (c[0] > c[1]):
        c[0] = c[1]


if __name__ == "__main__":
    # 入力
    N = None
    h = [None] * N
    for i in range(N):
        h[i] = int(input())
    
    # 初期化　（最小化問題なのでINFに初期化)
    dp = [INF] * N

    # 初期条件
    dp[0] = 0
    
    c = [] 
    # ループ
    for i in range(N):
        if (i + 1) < N:
            c = [dp[i + 1], dp[i] + abs(h[i + 1] - h[i])]
            chmin(c)
            dp[i + 1] = c[0]
        if (i + 2) < N:
            c = [dp[i + 2], dp[i] + abs(h[i + 2] - h[i])]
            chmin(c)
            dp[i + 2] = c[0]

    