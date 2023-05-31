""""""

import os
import shutil
import io


import PIL
from PIL import (
    ImageDraw,
    ImageFont,
)

import pathlib
from collections.abc import (  # noqa: F401 pylint: disable=W0611
    Callable as CA,
)
from collections.abc import (  # noqa: F401 pylint: disable=W0611
    Generator as GE,
)
from collections.abc import (  # noqa: F401 pylint: disable=W0611
    Iterable as IT,
)
from types import ModuleType as MT  # noqa: F401 pylint: disable=W0611

# Generator[YieldType, SendType, ReturnType]
from typing import Any as A  # noqa: F401 pylint: disable=W0611
from typing import Dict as D  # noqa: F401 pylint: disable=W0611
from typing import List as L  # noqa: F401 pylint: disable=W0611
from typing import Tuple as T  # noqa: F401 pylint: disable=W0611
from typing import Type as TY  # noqa: F401 pylint: disable=W0611
from typing import TypeAlias as TA
from typing import Union as U  # noqa: F401 pylint: disable=W0611

P: TA = pathlib.Path
B: TA = bool
F: TA = float
N: TA = None
O: TA = object
S: TA = str
Z: TA = int




BRAILLE = {
    0b00000000: chr(0x2800),
    0b10000000: chr(0x2801),
    0b00100000: chr(0x2802),
    0b10100000: chr(0x2803),
    0b00001000: chr(0x2804),
    0b10001000: chr(0x2805),
    0b00101000: chr(0x2806),
    0b10101000: chr(0x2807),
    0b01000000: chr(0x2808),
    0b11000000: chr(0x2809),
    0b01100000: chr(0x280A),
    0b11100000: chr(0x280B),
    0b01001000: chr(0x280C),
    0b11001000: chr(0x280D),
    0b01101000: chr(0x280E),
    0b11101000: chr(0x280F),
    0b00010000: chr(0x2810),
    0b10010000: chr(0x2811),
    0b00110000: chr(0x2812),
    0b10110000: chr(0x2813),
    0b00011000: chr(0x2814),
    0b10011000: chr(0x2815),
    0b00111000: chr(0x2816),
    0b10111000: chr(0x2817),
    0b01010000: chr(0x2818),
    0b11010000: chr(0x2819),
    0b01110000: chr(0x281A),
    0b11110000: chr(0x281B),
    0b01011000: chr(0x281C),
    0b11011000: chr(0x281D),
    0b01111000: chr(0x281E),
    0b11111000: chr(0x281F),
    0b00000100: chr(0x2820),
    0b10000100: chr(0x2821),
    0b00100100: chr(0x2822),
    0b10100100: chr(0x2823),
    0b00001100: chr(0x2824),
    0b10001100: chr(0x2825),
    0b00101100: chr(0x2826),
    0b10101100: chr(0x2827),
    0b01000100: chr(0x2828),
    0b11000100: chr(0x2829),
    0b01100100: chr(0x282A),
    0b11100100: chr(0x282B),
    0b01001100: chr(0x282C),
    0b11001100: chr(0x282D),
    0b01101100: chr(0x282E),
    0b11101100: chr(0x282F),
    0b00010100: chr(0x2830),
    0b10010100: chr(0x2831),
    0b00110100: chr(0x2832),
    0b10110100: chr(0x2833),
    0b00011100: chr(0x2834),
    0b10011100: chr(0x2835),
    0b00111100: chr(0x2836),
    0b10111100: chr(0x2837),
    0b01010100: chr(0x2838),
    0b11010100: chr(0x2839),
    0b01110100: chr(0x283A),
    0b11110100: chr(0x283B),
    0b01011100: chr(0x283C),
    0b11011100: chr(0x283D),
    0b01111100: chr(0x283E),
    0b11111100: chr(0x283F),
    0b00000010: chr(0x2840),
    0b10000010: chr(0x2841),
    0b00100010: chr(0x2842),
    0b10100010: chr(0x2843),
    0b00001010: chr(0x2844),
    0b10001010: chr(0x2845),
    0b00101010: chr(0x2846),
    0b10101010: chr(0x2847),
    0b01000010: chr(0x2848),
    0b11000010: chr(0x2849),
    0b01100010: chr(0x284A),
    0b11100010: chr(0x284B),
    0b01001010: chr(0x284C),
    0b11001010: chr(0x284D),
    0b01101010: chr(0x284E),
    0b11101010: chr(0x284F),
    0b00010010: chr(0x2850),
    0b10010010: chr(0x2851),
    0b00110010: chr(0x2852),
    0b10110010: chr(0x2853),
    0b00011010: chr(0x2854),
    0b10011010: chr(0x2855),
    0b00111010: chr(0x2856),
    0b10111010: chr(0x2857),
    0b01010010: chr(0x2858),
    0b11010010: chr(0x2859),
    0b01110010: chr(0x285A),
    0b11110010: chr(0x285B),
    0b01011010: chr(0x285C),
    0b11011010: chr(0x285D),
    0b01111010: chr(0x285E),
    0b11111010: chr(0x285F),
    0b00000110: chr(0x2860),
    0b10000110: chr(0x2861),
    0b00100110: chr(0x2862),
    0b10100110: chr(0x2863),
    0b00001110: chr(0x2864),
    0b10001110: chr(0x2865),
    0b00101110: chr(0x2866),
    0b10101110: chr(0x2867),
    0b01000110: chr(0x2868),
    0b11000110: chr(0x2869),
    0b01100110: chr(0x286A),
    0b11100110: chr(0x286B),
    0b01001110: chr(0x286C),
    0b11001110: chr(0x286D),
    0b01101110: chr(0x286E),
    0b11101110: chr(0x286F),
    0b00010110: chr(0x2870),
    0b10010110: chr(0x2871),
    0b00110110: chr(0x2872),
    0b10110110: chr(0x2873),
    0b00011110: chr(0x2874),
    0b10011110: chr(0x2875),
    0b00111110: chr(0x2876),
    0b10111110: chr(0x2877),
    0b01010110: chr(0x2878),
    0b11010110: chr(0x2879),
    0b01110110: chr(0x287A),
    0b11110110: chr(0x287B),
    0b01011110: chr(0x287C),
    0b11011110: chr(0x287D),
    0b01111110: chr(0x287E),
    0b11111110: chr(0x287F),
    0b00000001: chr(0x2880),
    0b10000001: chr(0x2881),
    0b00100001: chr(0x2882),
    0b10100001: chr(0x2883),
    0b00001001: chr(0x2884),
    0b10001001: chr(0x2885),
    0b00101001: chr(0x2886),
    0b10101001: chr(0x2887),
    0b01000001: chr(0x2888),
    0b11000001: chr(0x2889),
    0b01100001: chr(0x288A),
    0b11100001: chr(0x288B),
    0b01001001: chr(0x288C),
    0b11001001: chr(0x288D),
    0b01101001: chr(0x288E),
    0b11101001: chr(0x288F),
    0b00010001: chr(0x2890),
    0b10010001: chr(0x2891),
    0b00110001: chr(0x2892),
    0b10110001: chr(0x2893),
    0b00011001: chr(0x2894),
    0b10011001: chr(0x2895),
    0b00111001: chr(0x2896),
    0b10111001: chr(0x2897),
    0b01010001: chr(0x2898),
    0b11010001: chr(0x2899),
    0b01110001: chr(0x289A),
    0b11110001: chr(0x289B),
    0b01011001: chr(0x289C),
    0b11011001: chr(0x289D),
    0b01111001: chr(0x289E),
    0b11111001: chr(0x289F),
    0b00000101: chr(0x28A0),
    0b10000101: chr(0x28A1),
    0b00100101: chr(0x28A2),
    0b10100101: chr(0x28A3),
    0b00001101: chr(0x28A4),
    0b10001101: chr(0x28A5),
    0b00101101: chr(0x28A6),
    0b10101101: chr(0x28A7),
    0b01000101: chr(0x28A8),
    0b11000101: chr(0x28A9),
    0b01100101: chr(0x28AA),
    0b11100101: chr(0x28AB),
    0b01001101: chr(0x28AC),
    0b11001101: chr(0x28AD),
    0b01101101: chr(0x28AE),
    0b11101101: chr(0x28AF),
    0b00010101: chr(0x28B0),
    0b10010101: chr(0x28B1),
    0b00110101: chr(0x28B2),
    0b10110101: chr(0x28B3),
    0b00011101: chr(0x28B4),
    0b10011101: chr(0x28B5),
    0b00111101: chr(0x28B6),
    0b10111101: chr(0x28B7),
    0b01010101: chr(0x28B8),
    0b11010101: chr(0x28B9),
    0b01110101: chr(0x28BA),
    0b11110101: chr(0x28BB),
    0b01011101: chr(0x28BC),
    0b11011101: chr(0x28BD),
    0b01111101: chr(0x28BE),
    0b11111101: chr(0x28BF),
    0b00000011: chr(0x28C0),
    0b10000011: chr(0x28C1),
    0b00100011: chr(0x28C2),
    0b10100011: chr(0x28C3),
    0b00001011: chr(0x28C4),
    0b10001011: chr(0x28C5),
    0b00101011: chr(0x28C6),
    0b10101011: chr(0x28C7),
    0b01000011: chr(0x28C8),
    0b11000011: chr(0x28C9),
    0b01100011: chr(0x28CA),
    0b11100011: chr(0x28CB),
    0b01001011: chr(0x28CC),
    0b11001011: chr(0x28CD),
    0b01101011: chr(0x28CE),
    0b11101011: chr(0x28CF),
    0b00010011: chr(0x28D0),
    0b10010011: chr(0x28D1),
    0b00110011: chr(0x28D2),
    0b10110011: chr(0x28D3),
    0b00011011: chr(0x28D4),
    0b10011011: chr(0x28D5),
    0b00111011: chr(0x28D6),
    0b10111011: chr(0x28D7),
    0b01010011: chr(0x28D8),
    0b11010011: chr(0x28D9),
    0b01110011: chr(0x28DA),
    0b11110011: chr(0x28DB),
    0b01011011: chr(0x28DC),
    0b11011011: chr(0x28DD),
    0b01111011: chr(0x28DE),
    0b11111011: chr(0x28DF),
    0b00000111: chr(0x28E0),
    0b10000111: chr(0x28E1),
    0b00100111: chr(0x28E2),
    0b10100111: chr(0x28E3),
    0b00001111: chr(0x28E4),
    0b10001111: chr(0x28E5),
    0b00101111: chr(0x28E6),
    0b10101111: chr(0x28E7),
    0b01000111: chr(0x28E8),
    0b11000111: chr(0x28E9),
    0b01100111: chr(0x28EA),
    0b11100111: chr(0x28EB),
    0b01001111: chr(0x28EC),
    0b11001111: chr(0x28ED),
    0b01101111: chr(0x28EE),
    0b11101111: chr(0x28EF),
    0b00010111: chr(0x28F0),
    0b10010111: chr(0x28F1),
    0b00110111: chr(0x28F2),
    0b10110111: chr(0x28F3),
    0b00011111: chr(0x28F4),
    0b10011111: chr(0x28F5),
    0b00111111: chr(0x28F6),
    0b10111111: chr(0x28F7),
    0b01010111: chr(0x28F8),
    0b11010111: chr(0x28F9),
    0b01110111: chr(0x28FA),
    0b11110111: chr(0x28FB),
    0b01011111: chr(0x28FC),
    0b11011111: chr(0x28FD),
    0b01111111: chr(0x28FE),
    0b11111111: chr(0x28FF),
}




image = PIL.Image.open("font/00000000.png")

image = PIL.Image.open("demo.png")
image = image.resize((256, 256), PIL.Image.Resampling.LANCZOS)
image = image.convert("1")



WIDTH, HEIGHT = image.size
assert(WIDTH >= 2)
assert(HEIGHT >= 4)


length_x = WIDTH - 2
length_y = HEIGHT - 4

pixels = list(image.getdata())



string = io.StringIO()

def draw():

    def shift(offset_x, offset_y):
        nonlocal braille
        nonlocal range_x
        nonlocal range_y

        index_x = range_x + offset_x
        index_y = range_y + offset_y

        index = index_y * WIDTH + index_x
        pixel = pixels[index] // 255

        braille <<= 1
        braille |= pixel


    for range_y in range(0, HEIGHT - 4, 4):
        for range_x in range(0, WIDTH - 2, 2):
            braille = 0

            shift(0, 0)
            shift(1, 0)
            shift(0, 1)
            shift(1, 1)
            shift(0, 2)
            shift(1, 2)
            shift(0, 3)
            shift(1, 3)

            text = BRAILLE[braille]
            string.write(text)

        string.write("\n")


draw()
print(string.getvalue())
