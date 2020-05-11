numbers = [1,2,3]

p "filter method"
p numbers.select{|e| e > 1}

p "map method"
p numbers.map{|e| e.to_s}
p numbers.map(&:to_s)

p "map method - hash type list with symbol key"
p [{name:'A'},{name:'B'},{name:'C'}].map{|e| e[:name]}

p "map method - hash type list with string key"
p [{'name'=>'A'},{'name'=>'B'},{'name'=>'C'}].map{|e| e['name']}

p "reduce method"
p numbers.reduce(0){|sum, indv| sum + indv} 
p numbers.reduce(&:+)
