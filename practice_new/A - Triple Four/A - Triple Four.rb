n = gets.chomp.to_i
numbers = gets.chomp.split.map(&:to_i)

counter = 1

numbers.each_cons(2) do |prev, curr|
  counter = (prev == curr) ? counter + 1 : 1

  if counter == 3
    puts "Yes"
    exit
  end
end

puts "No"
