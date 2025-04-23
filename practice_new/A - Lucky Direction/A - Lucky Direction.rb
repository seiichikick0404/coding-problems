

direction_hash = {
  "N" => "S", "S" => "N",
  "E" => "W", "W" => "E",
  "NE" => "SW", "SW" => "NE",
  "SE" => "NW", "NW" => "SE"
}

puts direction_hash[gets.chomp]