numbers = [1,2,3]
d = {"a": 1, "b": 2, "c": 3}

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

p "iterate dictionary by key, value, both"
p "with keys"
d.each_key {|k| p k}

p "with values"
d.each_value {|v| p v}

p "with keys and values"
d.each {|k,v| p "#{k} #{v}" }

