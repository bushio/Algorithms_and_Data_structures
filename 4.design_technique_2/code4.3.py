# coding: utf-8
# 再帰呼出しが止まらない再帰関数
def func(N):
    if (N == 0):
        return 0
    return N + func(N + 1)

func(5) # RecursionError が発生する