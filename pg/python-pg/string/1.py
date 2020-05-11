line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re
# print(re.split(r'[;,\s]\s*', line))
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
print(re.split(r'(?:,|;|\s)\s*', line))
values = fields[::2]
delimiters = fields[1::2] + ['']

print(''.join(v + d for v, d in zip(values, delimiters)))

if 1:
    print('zero')
