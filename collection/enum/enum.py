from enum import Enum

print("the enum values must be declared")


class Color(Enum):
    red = 1
    green = 2
    blue = 3


print(Color.red)

print("enum name and value are printable")
print(Color.red.name)
print(Color.red.value)

print("it can be enumerated")
for c in Color:
    print(c)

print("programmatic access")
print(Color['red'])
print(Color(1))