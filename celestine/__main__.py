import PIL
import PIL.Image

from PIL import PngImagePlugin

PIL.Image.MAX_IMAGE_PIXELS = 9331200000

image = PIL.Image.open(r"C:\Users\mem_d\cross.png")

data = image.getdata()

black = 0
white = 0

for value in data:
	if value < 128:
		black += 1
	else:
		white += 1

print(black, white)