mod = 1000000007
N = int(input())  # サイコロの数
Answer = 1

# サイコロの各面の値を入力
A = [list(map(int, input().split())) for _ in range(N)]

# 各サイコロの面の値の合計を計算し、積を求める
for i in range(N):
    Answer *= sum(A[i])
    Answer %= mod

print(Answer)
