data = "cloudacademy.python.2019"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

#Split and Partition word
print(f"split = {data.split('.')}")
print(f"partition = {data.partition('python')}")

#Join on letter
print(f"join = {'*'.join(word1)}")
print(f"join = {'*'.join([letter1, word1, num1])}")

#Replace word/letter in string
print(f"replace = {data.replace('.','*')}")
print(f"replace = {data.replace(word1,num1)}")