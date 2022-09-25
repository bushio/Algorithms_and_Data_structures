# coding: utf-8
# 部分和問題を再帰関数を用いる全探索で解く

def func(i, w, a):
    # ベースケース
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    # a[i - 1]を選ばない場合
    if (func(i - 1, w, a)):
        return True
    
    # a[i - 1]を選ぶ場合
    if (func(i - 1, w - a[i-1], a)):
        return True
    
    # どちらも　false の場合は false
    return False

if __name__ == "__main__":
    # 入力
    N, W = list(map(int,input().split()))
    a = [None] * N
    for i in range(N):
        a[i] = int(input())
    
    # 再帰的に解く
    if (func(N, W, a)):
        print("Yes")
    else:
        print("No")
