# coding: utf-8

# Frog 問題に対する,　再帰関数を用いる単純な全探索
INF = 2**60

# c はaとbを格納したリスト (python ではポインタ渡しが不可なため)
def chmin(c: list):
    if (c[0] > c[1]):
        c[0] = c[1]


# rec(i): 足場 0 から足場 i までいたるまでの最小コスト
def rec(i):
    # 足場 0 のコストは 0
    if i == 0:
        return 0
    
    # 答えを格納する変数を INF に初期化する
    res = INF

    # 頂点 i - 1 から来た場合
    c = [res, rec(i-1) + abs(h[i] - h[i - 1]) ]
    chmin(c)
    res = c[0]

    # 頂点 i - 2 から来た場合
    c = [res, rec(i-2) + abs(h[i] - h[i - 2]) ]
    chmin(c)
    res = c[0]

    # 答えを返す
    return res
