# https://docs.python.org/3.3/tutorial/datastructures.html#sets

set1 = set()
print(f"set1 = {set1}")
print(f"data type = {type(set1)}")
print(f"length = {len(set1)}")

set2 = {"cloudacademy"}
print(f"set2 = {set2}")
print(f"data type = {type(set2)}")
print(f"length = {len(set2)}")

set3 = {1, 2, 3, 4, 5}
print(f"set3 = {set3}")
print(f"data type = {type(set3)}")
print(f"length = {len(set3)}")

set4 = {"cloud", "academy", 1, True, False}
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")

for item in set4:
    print(item)

print("cloud" in set4)
print("blah" in set4)

try:
    item0 = set4[0]
    item1 = set4[1]
    print(f"item0 = {item0}")
    print(f"item1 = {item1}")
except:
    print("Sets do not support indexing!!")

set4.add("devops")
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")

set4.add("devops")  # added prev
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")

set4.remove("cloud")
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")
