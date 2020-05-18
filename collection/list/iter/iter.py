
numbers = [1, 2, 3]
d = {"a": 1, "b": 2, "c": 3}

print("iterate list:")
for e in [1, 2, 3]:
    print(e)

print("iterate list with index:")
for i in range(len(numbers)):
    print(numbers[i], i)

print("iterate with both index and value")
for i, e in enumerate(numbers):
    print(e, i)

print("block is not pythonic, use regular function as argument instead:")


def larger_than_one(e):
    return e > 1


print(list(filter(larger_than_one, numbers)))

sum = 0
while sum < 3:
    sum += 1
print(sum)

