# https://docs.python.org/3.3/tutorial/datastructures.html#tuples-and-sequences

tup1 = ()
print(f"tup1 = {tup1}")
print(f"data type = {type(tup1)}")
print(f"length = {len(tup1)}")

tup2 = ("cloudacademy", )
print("CODE2:")
print(f"tup2 = {tup2}")
print(f"data type = {type(tup2)}")
print(f"length = {len(tup2)}")

tup3 = (1, 2, 3, 4, 5)
print(f"tup3 = {tup3}")
print(f"data type = {type(tup3)}")
print(f"length = {len(tup3)}")

tup4 = ("cloud", "academy", 1, True, False)
print(f"tup4 = {tup4}")
print(f"data type = {type(tup4)}")
print(f"length = {len(tup4)}")

for item in tup4:
    print(item)

item0 = tup4[0]
item1 = tup4[1]
print(f"item0 = {item0}")
print(f"item1 = {item1}")

try:
    tup4[0] = "not possible!"
except:
    print("Tuples are immutable!!")
