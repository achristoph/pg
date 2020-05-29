l = [1, 2, 3, 4, 5, 6]

print(l[:2] + l[2:])

s = 'bicycle'
print(s[::3])
print(s[::-1])

l = list(range(10))
l[2:5] = [20, 30]
print(l)
del l[2:4]
print(l)
l[3::2] = [100, 200]
print(l)