n = gets.chomp.to_i
numbers = gets.chomp.split.map(&:to_i)
total = 0
numbers.each_with_index do |num, i|
    total += num if (i+1) % 2 != 0
end

puts total
