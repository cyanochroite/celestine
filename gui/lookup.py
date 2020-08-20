import os

path = '.'
path = os.path.abspath(path)

print(path)
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.normpath(path))
print(os.path.normpath('.'))

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


mypath = os.path.normpath(path)
f = []
for (dirpath, dirnames, filenames) in os.walk(mypath):
    f.extend(filenames)
    break

for (path) in f:
    print("HI " + path)

print(f)
