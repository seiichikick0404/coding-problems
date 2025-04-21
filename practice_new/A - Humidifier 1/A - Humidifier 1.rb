n = gets.to_i

curr_water = 0
prev_time = 0

n.times do
  t, v = gets.split.map(&:to_i)

  # 前回の水追加から現在時刻までに減った分を引く
  elapsed = t - prev_time
  curr_water = [0, curr_water - elapsed].max

  # 水を追加
  curr_water += v

  # 今回の時間を記録
  prev_time = t
end

puts curr_water
