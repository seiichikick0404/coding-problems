n = gets.chomp.to_i
numbers = gets.chomp.split.map(&:to_i)

prev = numbers[0]
counter = 1
numbers.drop(1).each do |curr|
  if curr == prev
    counter += 1
    if counter == 3
      puts "Yes"
      exit
    end
  else
    counter = 1
  end
  prev = curr
end

puts "No"
