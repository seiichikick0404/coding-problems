n, c1, c2 = gets.chomp.split
n = n.to_i
S = gets.chomp.chars

ans = ""
for i in 0..n-1 do
    next if S[i] == c1

    S[i] = c2
end

puts S.join
