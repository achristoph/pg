# https://docs.python.org/3.3/tutorial/datastructures.html#more-on-lists
import array

list1 = []
list2 = ["cloudacademy"]
list3 = [1, 2, 3, 4, 5]
list4 = ["cloud", "academy", 1, True, False]

for item in list4:
    print(item)

print("cloud" in list4)
print("blah" in list4)

list4[0] = "possible!!"
list4.append("new item")

text = 'ABC'
# list comprehension
print([ord(s) for s in text])
# generator expression
print(tuple(ord(text) for text in text))
print(array.array('I', (ord(text) for text in text)))
