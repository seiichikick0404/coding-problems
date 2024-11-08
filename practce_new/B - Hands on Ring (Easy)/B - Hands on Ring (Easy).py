def get_clockwise_path(S, D, N):
    """
    現在位置 S から目的位置 D までの時計回りの経路をリストで返します（D は含まない）。
    """
    path = []
    current = S
    while current != D:
        current = current % N + 1  # 時計回りに移動
        if current != D:
            path.append(current)
    return path

def get_counterclockwise_path(S, D, N):
    """
    現在位置 S から目的位置 D までの反時計回りの経路をリストで返します（D は含まない）。
    """
    path = []
    current = S
    while current != D:
        current = (current - 2) % N + 1  # 反時計回りに移動
        if current != D:
            path.append(current)
    return path

def main():
    import sys

    # 入力の取得
    N, Q = map(int, sys.stdin.readline().split())
    questions = [tuple(sys.stdin.readline().split()) for _ in range(Q)]

    # 初期状態の設定
    left_pos = 1   # 左手の初期位置
    right_pos = 2  # 右手の初期位置
    total_steps = 0  # 総操作回数

    for H, T in questions:
        T = int(T)  # 目標パーツを整数に変換

        if H == 'L':
            S = left_pos
            O = right_pos
        else:
            S = right_pos
            O = left_pos

        D = T

        if S == D:
            steps = 0
        else:
            # 時計回りの経路と距離
            path_cw = get_clockwise_path(S, D, N)
            steps_cw = len(path_cw) + 1  # 目的地に到達するためのステップ数

            # 反時計回りの経路と距離
            path_ccw = get_counterclockwise_path(S, D, N)
            steps_ccw = len(path_ccw) + 1  # 目的地に到達するためのステップ数

            # 時計回りの経路に他の手が存在するかチェック
            if O in path_cw:
                can_take_cw = False
            else:
                can_take_cw = True

            # 反時計回りの経路に他の手が存在するかチェック
            if O in path_ccw:
                can_take_ccw = False
            else:
                can_take_ccw = True

            # 利用可能な経路の中で最小の操作回数を選択
            possible_steps = []
            if can_take_cw:
                possible_steps.append(steps_cw)
            if can_take_ccw:
                possible_steps.append(steps_ccw)

            if not possible_steps:
                # 問題文に「達成可能な指示しか与えられない」とあるため、ここに到達することはありません。
                print(-1)
                sys.exit()

            steps = min(possible_steps)

        # 総操作回数に加算
        total_steps += steps

        # 指定された手の位置を更新
        if H == 'L':
            left_pos = D
        else:
            right_pos = D

    # 結果の出力
    print(total_steps)

if __name__ == "__main__":
    main()
