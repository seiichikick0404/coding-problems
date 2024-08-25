def insertion_sort(a: list):
    N = len(a)
    for i in range(N-1):
        j = i + 1
        print(f'ソート済みインデックス:{i}')

        while i >= 0:
            if a[j] < a[i]:
                print(f'{a[i]} と {a[j]}をスワップ')
                a[i], a[j] = a[j], a[i]
                i -= 1
                j -= 1
            else:
                break

    return a


a = [5, 3, 1, 2, 4, 0]


print(insertion_sort(a))