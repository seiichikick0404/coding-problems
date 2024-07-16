def apply_operations(N, S, Q, operations):
    # 各文字が最終的にどの文字にマッピングされるかを保持する辞書を初期化
    char_map = {chr(ord('a') + i): chr(ord('a') + i) for i in range(26)}
    
    # 操作を適用して、マッピングを更新
    for c, d in operations:
        # すべてのキーに対して、もし値がcなら、それをdに変更する
        for key in char_map.keys():
            if char_map[key] == c:
                char_map[key] = d
    
    # 最終的な文字列を構築
    final_str = ''.join([char_map[ch] for ch in S])
    
    return final_str

N = int(input())
S = input()
Q = int(input())

operations =  []
for _ in range(Q):
    ci, di = input().split()
    operations.append((ci, di))

print(apply_operations(N, S, Q, operations))


