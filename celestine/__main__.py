import itertools

from pdf417gen import encode, render_image, render_svg

# Some data to encode
text = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Beautiful is better than ugly.

"""

import PIL

path = "D:\\OneDrive\\Pictures\\Doom\\Doom Screenshot 2020.01.16 - 09.52.58.59.png"
path = "D:\\file\\dot.png"
path = "D:\\file\\null.jpg"
image = PIL.Image.open(path)


text = bytes(itertools.chain.from_iterable(image.getdata()))

data = text
columns = 30
security_level = 0

codes = encode(data, columns, security_level)


# Generate barcode as image
image = render_image(codes)  # Pillow Image object
image.save('barcode.png')

# Generate barcode as SVG
svg = render_svg(codes)  # ElementTree object
svg.write("barcode.svg")


from PIL import Image as PIL
from pdf417decoder import PDF417Decoder


image = PIL.open("barcode.png")
decoder = PDF417Decoder(image)

if (decoder.decode() > 0):
    decoded = decoder.barcode_data_index_to_string(0)
    print("A", decoded)

cat = bytes((0, 0))
