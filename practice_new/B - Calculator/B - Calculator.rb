




S = gets.chomp
i = 0
count = 0

while i < S.length
  if S[i..i+1] == "00"
    i += 2
  else
    i += 1
  end
  count += 1
end

puts count
