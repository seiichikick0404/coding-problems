

n = gets.chomp.to_i
ans = ""

n.times do |i|
  center = n / 2

  if n.even?
    ans += (i == center - 1 || i == center) ? "=" : "-"
  else
    ans += (i == center) ? "=" : "-"
  end
end

puts ans




