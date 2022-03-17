import os


import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


path = '.'
path = os.path.abspath(path)

print(path)
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.normpath(path))
print(os.path.normpath('.'))
