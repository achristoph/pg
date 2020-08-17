from functools import wraps


# without pie syntax, decorate is just wrapper function
def log(f):
    def fn(*args, **kwargs):
        print("===")
        f(*args, **kwargs)
        print("===")

    return fn


def hi():
    print("Hi!")


# more verbose way to decorate hi()
hi = log(hi)
hi()


# using log decorator with pie syntax to decorate greet()
@log
def greet(name):
    print(f"Hello {name}")


greet("Joe")


# decorator with argument, needs a wrap function to accept original function
def log_with_options(sep):
    def wrap(old_fn):
        @wraps(old_fn)  # to help preserving original function attributes
        def new_fn(*args, **kwargs):
            print(sep)
            old_fn(*args, **kwargs)
            print(sep)

        return new_fn

    return wrap


# syntatic sugar: pie syntax
@log_with_options("---")
def hey():
    print("Hey!")


hey()
