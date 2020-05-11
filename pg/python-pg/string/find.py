data = "cloudacademy.python.2019"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

#Find word/letter in string
print(f"find '{letter1}' = {data.find(letter1)}")
print(f"find '{letter1}' = {data.find(letter1,6)}")
print(f"find '{word1}' = {data.find(word1)}")
print(f"index '{num1}' = {data.index(num1)}")

# Check string endswith and/or startswith another stringse
print(f"endswith = {data.endswith('2019')}")
print(f"startswith = {data.startswith(letter1)}")

# Is string alphanum, alpha, and/or digit
print(f"isalnum = {data.isalnum()}")
print(f"isalpha = {data.isalpha()}")
print(f"isdigit = {num1.isdigit()}")
