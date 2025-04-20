colors = gets.split.map{ |str| str.to_i }

hash = {}
colors.each do |color|
    if hash.key?(color)
        hash[color] += 1
    else
        hash[color] = 1
    end
end

total = 0
hash.each do | key, val |
    total += val / 2
end

puts total