import sys
import os
from datetime import datetime

if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    print("Syntax: %s directory" % sys.argv[0])
    sys.exit(1)

entries = [os.path.join(directory, file) for file in os.listdir(directory)]
print(entries)
files = [f for f in entries if os.path.isfile(f)]
print(files)
files = [[f, os.stat(f)[-2]] for f in files]
print(files)
sorted_files = sorted(files, key=lambda e: e[1])
print(sorted_files)
filetime = datetime.fromtimestamp(sorted_files[0][1])
print(filetime, sorted_files[0][0])