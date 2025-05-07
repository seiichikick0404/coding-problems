s = gets.chomp.chars
ans = ""

s.each do |char|
    ans += char if char.match?(/[A-Z]/)
end

puts ans