filename = 'spam.txt'
filename[-4:] == '.txt'

url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'

from fnmatch import fnmatch, fnmatchcase
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])

print(
    [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('11/27/2012')
print(m.group(0), m.group(1), m.group(2), m.group(3))
print(m.groups())

month, day, year = m.groups()
print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

for m in datepat.finditer(text):
    print(m.groups())
