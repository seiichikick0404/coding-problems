def main():
    n = int(input())
    # 空白で区切られた複数の数値を読み込んでaの値を設定
    a = [0] + list(map(int, input().split()))
    s, t = [0] * n, [0] * n

    for i in range(1, n):
        s[i], t[i] = map(int, input().split())

    for i in range(1, n):
        a[i + 1] += a[i] // s[i] * t[i]

    print(a[n])

if __name__ == "__main__":
    main()
