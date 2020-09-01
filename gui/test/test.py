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


array = ["!", "<", "=", ">"]
for a in array:
    print("#" + a)
    for b in array:
        print("#" + a + b)
        for c in array:
            print("#" + a + b + c)


import base64


a = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
a = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"


a = "19850412T101530Z"
a = "19850412"
b = bytearray()
b.extend(map(ord, a))
c = base64.b32encode(b)
print(c)


#d = 19850412
#d = 21001231235959
#d = 110510308215

z = [0, 1, 2, 3, 4, 5]
for d in range(33):
    e = d.to_bytes(1, "big")
    f = base64.b32encode(e)
    #print(d, e, f)

hh = [
    b'\x00', b'\x01', b'\x02', b'\x03',
    b'\x04', b'\x05', b'\x06', b'\x07',
    b'\x08', b'\x09', b'\x0A', b'\x0B',
    b'\x0C', b'\x0D', b'\x0E', b'\x0F',

    b'\x10', b'\x11', b'\x12', b'\x13',
    b'\x14', b'\x15', b'\x16', b'\x17',
    b'\x18', b'\x19', b'\x1A', b'\x1B',
    b'\x1C', b'\x1D', b'\x1E', b'\x1F',

    b'\x20', b'\x21', b'\x22', b'\x23',
    b'\x24', b'\x25', b'\x26', b'\x27',
    b'\x28', b'\x29', b'\x2A', b'\x2B',
    b'\x2C', b'\x2D', b'\x2E', b'\x2F',

    b'\x30', b'\x31', b'\x32', b'\x33',
    b'\x34', b'\x35', b'\x36', b'\x37',
    b'\x38', b'\x39', b'\x3A', b'\x3B',
    b'\x3C', b'\x3D', b'\x3E', b'\x3F',

    b'\x40', b'\x41', b'\x42', b'\x43',
    b'\x44', b'\x45', b'\x46', b'\x47',
    b'\x48', b'\x49', b'\x4A', b'\x4B',
    b'\x4C', b'\x4D', b'\x4E', b'\x4F',

    b'\x50', b'\x51', b'\x52', b'\x53',
    b'\x54', b'\x55', b'\x56', b'\x57',
    b'\x58', b'\x59', b'\x5A', b'\x5B',
    b'\x5C', b'\x5D', b'\x5E', b'\x5F',

    b'\x60', b'\x61', b'\x62', b'\x63',
    b'\x64', b'\x65', b'\x66', b'\x67',
    b'\x68', b'\x69', b'\x6A', b'\x6B',
    b'\x6C', b'\x6D', b'\x6E', b'\x6F',

    b'\x70', b'\x71', b'\x72', b'\x73',
    b'\x74', b'\x75', b'\x76', b'\x77',
    b'\x78', b'\x79', b'\x7A', b'\x7B',
    b'\x7C', b'\x7D', b'\x7E', b'\x7F',

    b'\x80', b'\x81', b'\x82', b'\x83',
    b'\x84', b'\x85', b'\x86', b'\x87',
    b'\x88', b'\x89', b'\x8A', b'\x8B',
    b'\x8C', b'\x8D', b'\x8E', b'\x8F',

    b'\x90', b'\x91', b'\x92', b'\x93',
    b'\x94', b'\x95', b'\x96', b'\x97',
    b'\x98', b'\x99', b'\x9A', b'\x9B',
    b'\x9C', b'\x9D', b'\x9E', b'\x9F',

    b'\xA0', b'\xA1', b'\xA2', b'\xA3',
    b'\xA4', b'\xA5', b'\xA6', b'\xA7',
    b'\xA8', b'\xA9', b'\xAA', b'\xAB',
    b'\xAC', b'\xAD', b'\xAE', b'\xAF',

    b'\xB0', b'\xB1', b'\xB2', b'\xB3',
    b'\xB4', b'\xB5', b'\xB6', b'\xB7',
    b'\xB8', b'\xB9', b'\xBA', b'\xBB',
    b'\xBC', b'\xBD', b'\xBE', b'\xBF',

    b'\xC0', b'\xC1', b'\xC2', b'\xC3',
    b'\xC4', b'\xC5', b'\xC6', b'\xC7',
    b'\xC8', b'\xC9', b'\xCA', b'\xCB',
    b'\xCC', b'\xCD', b'\xCE', b'\xCF',

    b'\xD0', b'\xD1', b'\xD2', b'\xD3',
    b'\xD4', b'\xD5', b'\xD6', b'\xD7',
    b'\xD8', b'\xD9', b'\xDA', b'\xDB',
    b'\xDC', b'\xDD', b'\xDE', b'\xDF',

    b'\xE0', b'\xE1', b'\xE2', b'\xE3',
    b'\xE4', b'\xE5', b'\xE6', b'\xE7',
    b'\xE8', b'\xE9', b'\xEA', b'\xEB',
    b'\xEC', b'\xED', b'\xEE', b'\xEF',

    b'\xF0', b'\xF1', b'\xF2', b'\xF3',
    b'\xF4', b'\xF5', b'\xF6', b'\xF7',
    b'\xF8', b'\xF9', b'\xFA', b'\xFB',
    b'\xFC', b'\xFD', b'\xFE', b'\xFF',

]

# for h in hh:
for hh in range(256):
    h = hh.to_bytes(1, "little")
    i = base64.b16encode(h)
    j = base64.b32encode(h)
    k = int.from_bytes(j, "big")
    print(h, i, j, k)

i = b'AH======'
g = base64.b32decode(i)
print(g)

# 2814 - 74 - 97T67: 10: 65: 5


# 658 - 97 - 12T42_83_73 + 6487
# 180 14 39 T 85 09 48 1984


# for h in hh:
k = ""
for hh in range(33, 127):
    t = chr(hh)
    k += t

print(k)

print(pow(2, 64))

# 18446 74 40 T 73 70 95 5 1616
# 1099511627776


import hashlib

print(hashlib.algorithms_guaranteed)

'sha3_256',
'sha3_224',
'sha3_384',
'sha3_512',
