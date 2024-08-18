A, B, C = map(int, input().split())

if B < C:  # 日をまたがない場合
    if B <= A < C:
        print("No")  # 高橋君は寝ている
    else:
        print("Yes")  # 高橋君は起きている
else:  # 日をまたぐ場合
    if A >= B or A < C:
        print("No")  # 高橋君は寝ている
    else:
        print("Yes")  # 高橋君は起きている


    