# required arguments must come first before those with default value
def addition(a, b=1):
    print(a * b)


print(addition(2))


# *args is tuple
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


print(multiply(4, 5))


# *kwargs is dict
def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


print_kwargs(kwargs_1="Shark", kwargs_2=4, kwargs_3=True)


def pass_tuple(a1, a2, a3):
    print(a1, a2, a3)


def pass_tuple1(a1, a2, a3):
    print(a1, args)


def pass_dict(a1, a2, a3):
    print(a1, a2, a3)


args = (1, 2, 3)
# pass_tuple(*args)
pass_tuple(1, *[2, 3])
# pass_dict({a: 1, b: 2, c: 3})
