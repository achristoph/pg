require 'set'

d = {"a": 1, "b": 2, "c": 3}

p "iterate dictionary with key, value, both"

p "with keys"
d.each_key {|k| p k}

p "with values"
d.each_value {|v| p v}

p "with keys and values"
d.each {|k,v| p "#{k} #{v}" }

set = Set.new([1,2,3])

set.each{|e| p e}
