s = gets.chomp

# 条件1: 長さが偶数でなければNo
if s.length.odd?
  puts "No"
  exit
end

# 条件2: 各文字が2回ちょうど出現
counts = s.chars.tally
unless counts.values.all? { |v| v == 2 }
  puts "No"
  exit
end

# 条件3: 隣り合う文字がすべて一致している
(0...s.length).step(2) do |i|
  if s[i] != s[i+1]
    puts "No"
    exit
  end
end

puts "Yes"

