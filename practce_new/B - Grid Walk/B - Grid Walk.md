## 考察
- X = L,R U,D なので現在の位置を記録しながら各値の処理を正しく行っていけば解ける
- 問題文に沿って適切な条件分岐を行えるかを問う問題

## 反省
最初マスの位置をindexベースで変換せずに進めたため条件作成時にout rangeエラーが何度も出てしまったので、
このような問題の場合は頭で理解しやすいようにindexベースに直すようにする