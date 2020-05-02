#Use Lambda and Map to double numbers in a list
numbers = [1, 4, 6, 7, 9, 1, 43, 2, 2]
doubledMap = map(lambda x: x * 2, numbers)
print(list(doubledMap))

# Use Lambda and Filter to split list of numbers into odds and evens
numbers = [0, 24, 3, 7, 5, 2, 634, 26, 8, 33, 333, 100]
odds = filter(lambda x: x % 2 != 0, numbers)
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(odds))
print(list(evens))
