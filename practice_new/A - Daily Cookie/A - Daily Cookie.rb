a, b = gets.split.map(&:to_i)

S = gets.chomp.chars

empty_box_count = 0
S.each do |s|
    if b != 0 && s == "@"
        empty_box_count += 1
        b -= 1
    end

    if s == "."
        empty_box_count += 1
    end
end

puts empty_box_count
