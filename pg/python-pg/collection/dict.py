# https://docs.python.org/3.3/tutorial/datastructures.html#dictionaries

dict1 = {}
print(f"dict1 = {dict1}")
print(f"data type = {type(dict1)}")
print(f"length = {len(dict1)}")

dict2 = {"name": "cloudacademy"}
print(f"dict2 = {dict2}")
print(f"data type = {type(dict2)}")
print(f"length = {len(dict2)}")

dict3 = {"name": "cloudacademy", "color": "red", "count": 1000}
print(f"dict3 = {dict3}")
print(f"data type = {type(dict3)}")
print(f"length = {len(dict3)}")

dict4 = {
    "name": "cloudacademy",
    "color": "red",
    "count": 1000,
    "data": {
        "val1": 1,
        "val2": 2
    }
}
print(f"set4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")

for key, value in dict4.items():
    print(f"key={key}, value={value}")

print("name" in dict4)
print("cloudacademy" in dict4)

item0 = dict4["name"]
item1 = dict4["color"]
print(f"item0 = {item0}")
print(f"item1 = {item1}")

#CODE8: Change existing value in DICTIONARY
print("CODE8:")
dict4["name"] = "blah"
dict4["color"] = "blue"
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

#CODE9: Add new key-value pair to DICTIONARY
print("CODE8:")
dict4['qwerty'] = 'fast'
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

#CODE10: Pop existing key-value pair from DICTIONARY
print("CODE10:")
test = dict4.pop('qwerty', None)
print(f"test = {test}")
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

#CODE11: Pop non-existing key-value pair from DICTIONARY
print("CODE11:")
test = dict4.pop('cat', None)
print(f"test = {test}")
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()