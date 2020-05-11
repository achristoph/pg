data = "cloudacademy.PYTHON.2019"
data_spaces = "     DevOps"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

#Strip format string
print(f"strip = {data_spaces.strip()}")
print(f"lstrip = {data.lstrip(word1)}")
print(f"rstrip = {data.rstrip(num1)}")

#Lower and upper case string
print(f"upper = {data.upper()}")
print(f"lower = {data.lower()}")

#Swap case string
print(f"swapcase = {data.swapcase()}")

#Title case string
print(f"title = {data.title()}")

#Center string
print(word1.center(20))
print(word1.center(20, '*'))

#Left and Right adjust string
print(word1.ljust(20, '*'))
print(word1.rjust(20, '*'))