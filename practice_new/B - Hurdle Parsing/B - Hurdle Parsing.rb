s = gets.chomp
# "|" で分割→空文字を除去→ダッシュの塊のみ残す
segments = s.split('|').reject(&:empty?)

# 各セグメントの長さを数えて出力
puts segments.map(&:length).join(' ')
