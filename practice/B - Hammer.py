



def main():
    x, y, z = map(int, input().split())

    # Yが負の場合は、X, Y, Zの符号を反転
    if y < 0:
        x = -x
        y = -y
        z = -z

    # XがYより小さい場合、直接Xに移動
    if x < y:
        print(abs(x))
    else:
        # ZがYより大きい場合、移動不可能
        if z > y:
            print(-1)
        else:
            # ハンマーを取りに行ってからXに移動
            print(abs(z) + abs(x - z))

# 関数の実行
main()



