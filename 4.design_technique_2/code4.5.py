# coding: utf-8
# フィボナッチ数列を求める再帰関数
def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fibo(N-1) + fibo (N-2)
print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))