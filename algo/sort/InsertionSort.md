## ポイント
- insertion sortはソート済みと未ソート部分に分けて少しずつsort済み範囲を広げていく手法
- 最悪の計算量はO(N2)の安定ソート


```python
def insertion_sort(a: list):
    N = len(a)
    for i in range(N-1):
        j = i + 1

        while i >= 0:
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
                i -= 1
                j -= 1
            else:
                break

    return a
```

## 解説
- forループでソート済みの範囲を確定していく
- whileループでソート済み末尾とその+1の値を-1インデックスずつ比較していき、+1の値の方が大きい場合スワップする
- whileループの停止はa[i]の方が大きい場合、つまり現在のiの範囲では既にソートが完了してるとき