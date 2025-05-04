a, b, c = gets.chomp.split.map(&:to_i)

if a == b + c || b == a + c || c == a + b || (a == b && b == c)
    puts "Yes"
  else
    puts "No"
  end



