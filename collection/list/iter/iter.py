
numbers = [1, 2, 3]
d = {"a": 1, "b": 2, "c": 3}

print("iterate list")
for e in [1, 2, 3]:
    print(e)

print("iterate list with index")
for i in range(len(numbers)):
    print(numbers[i], i)

for i, e in enumerate(numbers):
    print(e, i)

print("iterate dictionary by key, value, both")
print("with keys")
for k in d:
    print(k)

for k in d.keys():
    print(k)

print("with values")
for k in d.values():
    print(k)

print("with keys and values")
for k, v in d.items():
    print(k, v)

print("block is not pythonic, use regular function as argument instead")


def larger_than_one(e):
    return e > 1


print(list(filter(larger_than_one, numbers)))
