
# coding: utf-8
# 1からNまでの総和を計算する再帰関数
def func(N):
    if (N == 0):
         return 0
    return N + func(N - 1)


print(func(0)) # 0
print(func(1)) # 1
print(func(2)) # 3
print(func(3)) # 6
print(func(4)) # 10
print(func(5)) # 15