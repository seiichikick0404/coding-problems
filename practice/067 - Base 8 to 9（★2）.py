def main():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline

    N, K = map(str, input().split(" "))

    def basen_to_10(num_n, n):  # n進数→10進数に変換
        if num_n == 0:
            return 0
        num_10 = 0
        for s in str(num_n):
            num_10 *= n
            num_10 += int(s)
        return num_10

    def base10_to_n(num_10, n):  # 10進数→n進数に変換
        if num_10 == 0:
            return 0
        str_n = ''
        while num_10:
            if num_10 % n >= 10:
                return -1
            str_n += str(num_10 % n)
            num_10 //= n
        return int(str_n[::-1])

    K = int(K[:-1])  # K[:-1]としているのは私がinput関数をsys.stdin.readlineで置き換えて使用しているため。通常はKでOKです。
    for _ in range(K):
        N = basen_to_10(N, 8)  # 8進数→10進数に変換
        N = base10_to_n(N, 9)  # 10進数→9進数に変換
        N = int(str(N).replace('8', '5'))  # 8を5に変換

    print(N)


if __name__ == '__main__':
    main()