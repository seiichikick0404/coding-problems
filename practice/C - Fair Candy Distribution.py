N, K = map(int, input().split())

my_number = list(map(int, input().split()))
indexed_numbers = list(enumerate(my_number))

indexed_numbers.sort(key=lambda x: x[1])



ans = [0 for _ in range(N)]

# 全員に均等に配る
j = K // N
for i in range(N):
    ans[i] = j

# 残りを配る
K = K % N
for i in range(K):
    ans[indexed_numbers[i][0]] += 1


for count in ans:
    print(count)

