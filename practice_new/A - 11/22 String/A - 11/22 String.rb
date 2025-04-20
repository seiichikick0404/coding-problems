n = gets.to_i
s = gets.chomp

# 条件1: 長さが奇数かどうか
if n.even?
  puts "No"
  exit
end

mid = n / 2

# 条件2: 真ん中が '/'
if s[mid] != '/'
  puts "No"
  exit
end

# 条件3: 前半が全部 '1'、後半が全部 '2'
left = s[0...mid]
right = s[(mid+1)..]

if left.chars.all? { |c| c == '1' } && right.chars.all? { |c| c == '2' }
  puts "Yes"
else
  puts "No"
end



