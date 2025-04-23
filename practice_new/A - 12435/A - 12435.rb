
numbers = gets.chop.split.map(&:to_i)
sorted = [1, 2, 3, 4, 5]
for i in 0..3
    swapped = numbers.dup
    swapped[i], swapped[i+1] = swapped[i+1], swapped[i]

    if swapped == sorted
        puts 'Yes'
        exit
    end
end


puts 'No'