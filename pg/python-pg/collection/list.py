# https://docs.python.org/3.3/tutorial/datastructures.html#more-on-lists

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

l = [10, 20, 30, 40, 50, 60]
print(l[:2], l[2:])

s = 'bicycle'
print(s[::3], s[::-1])
