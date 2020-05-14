# Ruby does not have enum, we can use module instead, and must be capitalized
module Color
  Red = 1
  Green = 2
  Blue = 4
end

p Color::Red
