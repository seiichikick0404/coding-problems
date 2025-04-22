cards = gets.chomp.split.map(&:to_i)  # スペース区切りで5枚のカードを取得

def is_full_house?(hand)
  counts = hand.tally.values.sort
  counts == [2, 3]
end

# 1〜9のカードを1枚ずつ追加して試す
(1..9).each do |extra_card|
  new_cards = cards + [extra_card]

  # 6枚中から5枚の組み合わせをすべて調べる
  new_cards.combination(5).each do |hand|
    if is_full_house?(hand)
      puts "Yes"
      exit
    end
  end
end

# 全パターン調べてもフルハウスができなかったら
puts "No"
