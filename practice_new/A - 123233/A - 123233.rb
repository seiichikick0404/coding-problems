N = gets.chomp

digits = N.chars.map(&:to_i)  # 各桁を整数の配列にする

count = Hash.new(0)
digits.each { |d| count[d] += 1 }

if count[1] == 1 && count[2] == 2 && count[3] == 3
  puts "Yes"
else
  puts "No"
end
