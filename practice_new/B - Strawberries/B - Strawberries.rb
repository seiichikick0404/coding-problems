

n, k = gets.chomp.split.map(&:to_i)
s_list = gets.chomp.chars

total = 0

i = 0
while i <= n - k
  # K 本連続で "O" なら
  if s_list[i, k].all? { |ch| ch == "O" }
    total += 1
    # 虫歯にする
    k.times { |j| s_list[i + j] = "X" }
    i += k  # 次の非重複エリアへスキップ
  else
    i += 1
  end
end

puts total

