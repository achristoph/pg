#  Comparator functions

# Ruby has spaceship operator that return 0,1,-1 for equal, greater than and less than comparison
def by_lower_case(a,b)
  return a.downcase <=> b.downcase
end

def by_length(a,b)
  return a.length <=> b.length
end

# new sorted array
a = ['Art', 'b', 'ART']

# 1. Creating a new sorted array with a comparator
b = a.sort {|a,b| by_lower_case(a,b) }
p(b)

# 2. Creating a new sorted array with multiple comparators
c = a.sort {|a,b|  by_length(a,b) || by_lower_case(a,b) }
p(c)

# 3. Sorting array with in-place sort
# Ruby uses exclamation point to warn that the original object is mutated
a.sort! {|a,b|  a.downcase <=> b.downcase}
# Ruby has a convenient method sort_by
a.sort_by!(&:length)
a.sort_by! { |e| e.length }
p a
# multiple fields sort
p [{ :name=>"BA", :count=>1},{:name=>"B",:count=>10},{:name=>"B",:count=>1}].sort_by { |e| [e[:name],e[:count]] }

# 4. Sorting numeric array to string order
d = [2, 100, 3]
a.sort! {|a,b| by_lower_case(a,b) }
# alternate method
d.sort_by!(&:to_s)
p(d)

# 5. Sorting string array to numeric order
e = ['2', '100', '3']
e.sort! {|a,b| by_lower_case(a,b) }
# alternate method
e.sort_by!(&:to_i)
p(e)

# 6. Sorting numeric array
f = [3, 1, 2]
f.sort!
p(f)