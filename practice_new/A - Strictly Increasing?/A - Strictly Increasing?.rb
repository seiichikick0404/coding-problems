n = gets.chomp.to_i
numbers = gets.chomp.split.map(&:to_i)

# 入力された配列の長さがnと一致しているか確認（安全策）
if numbers.size != n
  puts "入力された数が指定された個数と違います"
  exit
end

numbers.each_cons(2) do |a, b|
  if a >= b  # 「狭義単調増加」なので、a < b でなければNG
    puts "No"
    exit
  end
end

puts "Yes"
