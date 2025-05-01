n = gets.chomp.to_i
s = gets.chomp
t = gets.chomp

count = 0
n.times do |i|
    count += 1  if s[i] != t[i]
end

puts count