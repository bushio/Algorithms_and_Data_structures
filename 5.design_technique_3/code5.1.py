# coding: utf-8
# Frog問題を動的計画法で解く
INF = 2^60

if __name__ == "__main__":
    # 入力
    N = int(input())
    h = [None] * N
    for i in range(N):
        h[i] = int(input())
    
    # 配列 dp を定義 (配列全体を無限大を表す値に初期化)
    dp = [INF] * N

    # 初期条件
    dp[0] = 0

    # ループ
    for i in range(1, N):
        if i == 1:
            dp[i] = abs(h[i] - h[i- 1])
        else:
            dp[i] = min (dp[i-1] + abs(h[i] - h[i- 1]),
                dp[i-2] +  abs(h[i] - h[i- 2]))
    print(dp[N-1])
    