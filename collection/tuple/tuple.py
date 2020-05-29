import array

text = 'ABC'
# list comprehension
print([ord(s) for s in text])
# generator expression
print(tuple(ord(text) for text in text))
print(array.array('I', (ord(text) for text in text)))
