# https://docs.python.org/3.3/tutorial/datastructures.html#more-on-lists

list1 = []
print(f"list1 = {list1}")
print(f"data type = {type(list1)}")
print(f"length = {len(list1)}")

list2 = ["cloudacademy"]
print(f"list2 = {list2}")
print(f"data type = {type(list2)}")
print(f"length = {len(list2)}")

list3 = [1, 2, 3, 4, 5]
print(f"list3 = {list3}")
print(f"data type = {type(list3)}")
print(f"length = {len(list3)}")

list4 = ["cloud", "academy", 1, True, False]
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")

for item in list4:
    print(item)

print("cloud" in list4)
print("blah" in list4)

list4[0] = "possible!!"
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")

list4.append("new item")
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")
