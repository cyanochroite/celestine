""""""

import colorsys

import PIL
import PIL.Image


colours = []

choices = [index * 256 / 7 for index in range(8)]
crayola = []


def sorter(value):
    h0, s0, v0 = value
    croma1 = max(h0, s0, v0) - min(h0, s0, v0)
    h1, s1, v1 = colorsys.rgb_to_hls(
        h0 / 256,
        s0 / 256,
        s0 / 256,
    )
    h2 = round(h1, 2)
    s2 = round(s1, 2)
    v2 = round(v1, 2)
    cr2 = round(croma1 / 256, 2)
    cat = f"{v2}_{cr2}_{h2}"
    cat = f"{v2 * cr2* cr2}_{h2}"
    magic0 = round(1000 * (v2 * cr2 * cr2) + (360 * v2))
    magic = str(magic0).zfill(5)
    return magic


limit = 8

red = []
green = []
blue = []
cyan = []
magenta = []
yellow = []
grey = []

counter = 0
for rr in range(limit):
    for gg in range(limit):
        for bb in range(limit):
            counter += 1
            pixel = (rr, gg, bb)
            big = max(rr, gg, bb)
            low = min(rr, gg, bb)

            if rr == gg and gg == bb:
                grey.append(pixel)
                continue

            if rr == gg:
                if bb > rr:
                    blue.append(pixel)
                else:
                    yellow.append(pixel)
                continue

            if gg == bb:
                if rr > gg:
                    red.append(pixel)
                else:
                    cyan.append(pixel)
                continue

            if bb == rr:
                if gg > bb:
                    green.append(pixel)
                else:
                    magenta.append(pixel)
                continue

            def findit(aa, oo, cc):

                sorter = [rr, gg, bb]
                sorter.sort()
                small = sorter[0]
                big = sorter[1]
                isitus = sorter[2]
                if aa != isitus:
                    return
                first = aa - big
                second = big - small
                if first > second:
                    oo.append(pixel)
                if first < second:
                    cc.append(pixel)
                if first == second:
                    total = rr + gg + bb + 3
                    compore = limit + limit + limit
                    if total + total > compore:
                        cc.append(pixel)
                    else:
                        oo.append(pixel)

            findit(rr, red, cyan)
            findit(gg, green, magenta)
            findit(bb, blue, yellow)


print(counter)
print(len(red))
print(len(green))
print(len(blue))
print(len(magenta))
print(len(yellow))
print(len(cyan))
print(len(grey))
print(3 / 0)
for red in choices:
    for green in choices:
        for blue in choices:
            big = max(red, green, blue)
            small = min(red, green, blue)
            croma = big - small
            hh, ss, vv = colorsys.rgb_to_hls(
                red / 256,
                green / 256,
                blue / 256,
            )
            colours.append((hh, ss, vv))
            valuess = red + green + blue
            print(valuess)
            if red + green + blue < 400:
                continue
            crayola.append(
                (
                    round(red),
                    round(green),
                    round(blue),
                )
            )

crayola.sort(key=sorter)


print(len(colours), len(crayola))
length = len(crayola) - 1
image = PIL.Image.new("RGB", (1024, 1024))
for y in range(1024):
    for x in range(1024):
        xx = x // 4
        yy = min(xx, length)
        colour = crayola[yy]
        image.putpixel((x, y), colour)

image.show()
