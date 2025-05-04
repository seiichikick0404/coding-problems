n, d = gets.chomp.split.map(&:to_i)
snakes = []

n.times do
    t, l = gets.chomp.split.map(&:to_i)
    snakes << [t, l]
end

(1..d).each do |k|
    max_weight = snakes.map { |t, l| t * (l + k) }.max
    puts max_weight
end

3.times { puts "Hi" }