n = [1,2,3]

# Array constructor with a default value
a = Array.new(2,0)
# if initialize with object, it refers to the same object
a = Array.new(2,[])
a[0].push(1)

# instead, use block to pass object 
a = Array.new(2) { [] }
a[0].push(1)

# construct a multi-dimensional array
a = Array.new(3) { Array.new(3) }

# accessing elements
a = [1, 2, 3, 4]
# single element
p a[0]
p a.at(0)
# start index and how many elements
p a[0,3]
# range, inclusive of both start and end index
p a[0..2]

