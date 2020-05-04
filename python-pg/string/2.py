filename = 'spam.txt'
filename.endswith('.txt')

print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

import os
filenames = os.listdir('.')
print(filenames)
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(tuple(choices))
