def function_1(self):
    print("Hello from f1()")


def function_2(self):
    print("Hello from f2()")


# Define a new class named NewClass using the builtin type function
NewClass = type("new_class", (object, ), {
    'hello1': function_1,
    'hello2': function_2,
    'color': 'red',
    'state': 'Ohio',
})

# Instantiate the NewClass object and test it out
n1 = NewClass()
n1.hello1()
n1.hello2()
print(n1.color)

# Define a new class named SubClass which inherits from the NewClass class using the builtin type function
SubClass = type("sub_class", (NewClass, ), {'fruit': 'banana'})

s1 = SubClass()
s1.hello1()
print(s1.color)
print(s1.fruit)
