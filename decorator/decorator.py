def log(func):
    def wrapper(*args, **kwargs):
        print("===")
        func(*args, **kwargs)
        print("===")

    return wrapper


def hi():
    print("Hi!")


hi = log(hi)
hi()

print("pie syntax")


# syntatic sugar: pie syntax
@log
def hey():
    print("Hey!")


hey()


@log
def greet(name):
    print(f"Hello {name}")


greet("Joe")