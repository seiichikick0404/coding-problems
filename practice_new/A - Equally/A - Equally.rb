
a, b, c = gets.chomp.split.map(&:to_i)
case_one = a + b
case_two = a + c

puts(case_one == c || case_two == b ? "Yes" : "No")
