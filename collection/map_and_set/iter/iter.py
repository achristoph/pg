
d = {"a": 1, "b": 2, "c": 3}

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

print("iterate set")
set = {1,2,3}
for e in set:
    print(e)
