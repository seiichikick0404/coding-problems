# def find_in_order(A, B, nums):


N = int(input())
nums = list(map(int, input().split()))
Q = int(input())
Q_list = []


for i in range(Q):
    A, B = map(int, input().split())
    Q_list.append((A, B))

hash_map = {}
for i in range(N):
    hash_map[nums[i]] = i

for q in Q_list:
    if hash_map[q[0]] < hash_map[q[1]]:
        print(q[0])
    else:
        print(q[1])