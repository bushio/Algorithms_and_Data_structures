# coding: utf-8
# フィボナッチ数列をfor 文による反復で求める

if __name__ == "__main__":
    F = [None] * 50
    F[0] = 0
    F[1] = 1
    for N in range(2, 50):
        F[N] = F[N - 1] + F[N - 2]
        print("{} 項目 = {}".format(N, F[N]))