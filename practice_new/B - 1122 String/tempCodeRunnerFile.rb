words = gets.chomp.chars

if words.length.odd?
    puts "No"
    exit

hash = Hash.new(0)
words.each do |char|
    hash[char] += 1
end

hash.each do |key, value|
    if value != 2
        puts "No" 
        exit
    end
end

puts "Yes"