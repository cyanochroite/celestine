""""""

import os
import sys

import PIL
import PIL.Image

sys.path[0] = os.path.dirname(sys.path[0])


# celestine = __import__("celestine")
# celestine.main(sys.argv[1:], True)


palettedata = [
    0x00,
    0x0F,
    0x1E,
    0x2D,
    0x3C,
    0x4B,
    0x5A,
    0x69,
    0x78,
    0x87,
    0x96,
    0xA5,
    0xB4,
    0xC3,
    0xD2,
    0xE1,
    0xF0,
    0xFF,
]

ASCII_CHARS = [
    ".",
    "`",
    "'",
    ",",
    "-",
    ";",
    "^",
    "!",
    '"',
    "+",
    "=",
    "*",
    "?",
    "%",
    "#",
    "&",
    "$",
    "@",
]

ASCII_CHARS = [
    "@",
    "$",
    "&",
    "#",
    "%",
    "?",
    "*",
    "=",
    "+",
    '"',
    "!",
    "^",
    ";",
    "-",
    ",",
    "'",
    "`",
    ".",
]


"""
Method modify():

    - replaces every pixel with a character whose intensity is similar
"""


def modify(image):
    initial_pixels = list(image.getdata())
    new_pixels = [
        ASCII_CHARS[pixel_value // 15] for pixel_value in initial_pixels
    ]
    return "".join(new_pixels)


"""
method do():
    - does all the work by calling all the above functions
"""


def do(image, new_width=100):
    (x, y) = image.size

    width = 128 * max(x / y, 1)
    height = 128 * max(y / x, 1)

    image = image_resize(image, width, height)
    image = image_quantize(image)
    image = image_convert(image, "L")

    image.save("test.png")

    pixels = modify(image)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [
        pixels[index : index + new_width]
        for index in range(0, len_pixels, new_width)
    ]

    return "\n".join(new_image)


"""
method runner():
    - takes as parameter the image path and runs the above code
    - handles exceptions as well
    - provides alternative output options
"""


def runner(path):
    image = None
    try:
        image = PIL.Image.open(path)
        image = image_convert(image, "RGB")
    except Exception:
        print("Unable to find image in", path)
        # print(e)
        return
    image = do(image)

    # To print on console
    print(image)

    # Else, to write into a file
    # Note: This text file will be created by default under
    #       the same directory as this python file,
    #       NOT in the directory from where the image is pulled.
    f = open("img.txt", "w")
    f.write(image)
    f.close()


######

PALETTE = PIL.Image.new("P", (1, 1))
PALETTE.putpalette(
    [
        0x00,
        0x00,
        0x00,
        0x0F,
        0x0F,
        0x0F,
        0x1E,
        0x1E,
        0x1E,
        0x2D,
        0x2D,
        0x2D,
        0x3C,
        0x3C,
        0x3C,
        0x4B,
        0x4B,
        0x4B,
        0x5A,
        0x5A,
        0x5A,
        0x69,
        0x69,
        0x69,
        0x78,
        0x78,
        0x78,
        0x87,
        0x87,
        0x87,
        0x96,
        0x96,
        0x96,
        0xA5,
        0xA5,
        0xA5,
        0xB4,
        0xB4,
        0xB4,
        0xC3,
        0xC3,
        0xC3,
        0xD2,
        0xD2,
        0xD2,
        0xE1,
        0xE1,
        0xE1,
        0xF0,
        0xF0,
        0xF0,
        0xFF,
        0xFF,
        0xFF,
    ]
)


def image_convert(image, mode):
    """"""

    matrix = None
    dither = PIL.Image.Dither.NONE
    palette = PIL.Image.Palette.WEB
    colors = 256

    result = image.convert(mode, matrix, dither, palette, colors)

    return result


def image_resize(image, width, height):
    """"""

    size = (round(width), round(height))
    resample = PIL.Image.Resampling.LANCZOS
    box = None
    reducing_gap = None

    result = image.resize(size, resample, box, reducing_gap)

    return result


def image_quantize(image):
    """"""

    colors = 256
    method = None
    kmeans = 0
    palette = PALETTE
    dither = PIL.Image.Dither.NONE

    result = image.quantize(colors, method, kmeans, palette, dither)

    return result


if __name__ == "__main__":
    path = sys.argv[1]
    runner(path)


items = []


def work(name):
    global items

    black = 0
    white = 0
    path = sys.argv[1]
    file = ""
    file = f"{path}\\{name}.png"

    image = PIL.Image.open(file)
    image = image.convert("1")

    initial_pixels = list(image.getdata())

    for pixel_value in initial_pixels:
        if pixel_value == 0:
            black += 1
        elif pixel_value == 255:
            white += 1
        else:
            raise RuntimeError()

    items.append((black, name))


for index in range(23):
    name = str(index).zfill(2)
    work(name)

items = sorted(items)

for item in items:
    print(item[0], item[1])

print("$$$$")
contrast = []

last = 0
for item in items:
    diff = item[0] - last
    print(diff, item[1])
    last = item[0]
