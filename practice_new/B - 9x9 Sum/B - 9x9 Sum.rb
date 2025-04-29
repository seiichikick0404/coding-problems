
x = gets().to_i
total = 0
(1..9).each do |i|
    (1..9).each do |j|
        curr = i * j
        if curr != x
            total += curr
        end
    end
end

puts total

