N, T = map(int, input().split())

song_lengths = list(map(int, input().split()))

total_duration = sum(song_lengths)

# T秒後のプレイリスト内の位置
position = T % total_duration

print("T秒後のポジション：", position)

# その時間に流れている曲を探す
elapsed_time = 0
for i, length in enumerate(song_lengths):
    if elapsed_time + length > position:
        # 曲番号と再生開始からの経過時間を返す。
        print(i + 1, position - elapsed_time)
        exit()
    elapsed_time += length
