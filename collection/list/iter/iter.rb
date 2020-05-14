numbers = [1,2,3]

p "iterate list" 
for e in numbers do
  p e
end

numbers.each {|e| p e}

p "iterate list with index"
numbers.each_with_index {|e,i| p "#{e} #{i}"}

p "with block"
x = numbers.each do |e|
  p e
end

sum = 0
while sum < 3
  sum += 1
end
p sum

