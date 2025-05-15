

x = gets.chomp.to_i

fact = 1
n = 1

while true
  fact *= n         # n! を計算（前の階乗に n をかける）
  if fact == x     # 一致したら答えが見つかった！
    puts n
    break
  end
  n += 1            # 次の n へ
end