
import functools

numbers = [1,2,3]
print("filter method")
print(list(filter(lambda e: e > 1, numbers)))

print("map method")
print(list(map(lambda e: str(e), numbers)))

print("list comprehension")
print([str(e) for e in numbers])

print("map method - dict type list")
d = [{"name": "A"}, {"name": "B"}, {"name": "C"}]
print(list(map(lambda e: e["name"], d)))
print([e["name"] for e in d])

print("reduce method")
print(functools.reduce(lambda a, b: a + b, numbers))
