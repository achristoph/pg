#  Comparator functions
def by_lower_case(e):
    return e.lower()


def by_length_then_name(item):
    return (len(item), item.lower())


a = ['Art', 'b', 'ART']

# 1. Creating a new sorted array with a comparator
b = sorted(a, key=by_lower_case)
print(b)

# 2. Creating a new sorted array with multiple comparators
c = sorted(a, key=by_length_then_name)
print(c)

# 3. Sorting array with in-place sort
a.sort(key=by_lower_case)
print(a)

# 4. Sorting numeric array to string order
d = [2, 100, 3]
d.sort(key=str)
print(d)

# 5. Sorting string array to numeric order
e = ['2', '100', '3']
e.sort(key=int)
print(e)
