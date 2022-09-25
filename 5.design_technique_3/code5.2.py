# coding: utf-8

# 緩和処理を実現するための関数 chmin
# c はaとbを格納したリスト (python ではポインタ渡しが不可なため)
def chmin(c: list):
    if (c[0] > c[1]):
        c[0] = c[1]
