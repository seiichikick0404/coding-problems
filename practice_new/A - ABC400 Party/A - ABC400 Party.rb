n = gets.chomp.to_i

if 400 % n != 0
    puts -1
else
    puts 400 / n
end