import itertools

from pdf417gen import encode, render_image, render_svg

# Some data to encode
text = """
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
Beautiful is better than ugly. Explicit is better than implicit. Simp is better.
"""

text = """Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. Explicit is better than implicit. Simp is better.Beautiful is better than ugly. is 42eu."""

import PIL

from pylibdmtx.pylibdmtx import encode, decode

path = "D:\\OneDrive\\Pictures\\Doom\\Doom Screenshot 2020.01.16 - 09.52.58.59.png"
path = "D:\\file\\color.png"
# path = "D:\\file\\null.jpg"
image = PIL.Image.open(path)



text1 = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
C"""

text = bytes(itertools.chain.from_iterable(image.getdata()))


text = ['0', 'F', 'F', 'A', '5', '4']
text = "ABCDEF"


count = 0
text = []
for index in range(32, 127):
    count += 1
    text.append(chr(index))
    text.append(str(index))
text = "".join(text)
print(text)
print(count)

import base64
import random
text = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
text = text.encode("utf8")
cat = base64.a85encode(text)
print(cat)
data = text
scheme = "Base2561"
size = "144x144"



def convert(self, mode):
    """"""
    mode = "RGBA"
    matrix = None
    dither = PIL.Image.Dither.NONE
    palette = PIL.Image.Palette.WEB
    colors = 256
    return image.convert(mode, matrix, dither, palette, colors)


scheme = None
size = None

text = random.randbytes(1244)
# text = text.encode("utf8")
data = base64.a85encode(text, pad=True)

encoded = encode(data, scheme, size)

img = PIL.Image.frombytes(
    'RGB', (encoded.width, encoded.height), encoded.pixels)

img.save('dmtx.png')


print(decode(PIL.Image.open('dmtx.png')))


from pylibdmtx.pylibdmtx import decode
from PIL import Image
carwash = decode(Image.open('dmtx.png'))
print(carwash)
print(carwash[0][0])
print(carwash[0][1])
cat = 0

