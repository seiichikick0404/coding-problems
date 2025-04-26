s = gets.chomp.chars.map(&:to_i)

ans = []
s.each do | num |
    next if num != 2
    ans << num
end

puts ans.join()
