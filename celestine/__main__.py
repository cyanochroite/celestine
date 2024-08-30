import PIL
import PIL.Image
import math

a = 978900
b = 255310
c = 221105

a *= math.sqrt(2)
b *= math.sqrt(2)
c *= math.sqrt(2)

ba = b / a # 0.2608131576
ca = c / a # 0.2258708754

testa = 0.0000152
testb = 0.0000152
limit = 2500

testa = 0.000044299
testb = 0.000044299
limit = 1000

testa = 0.0001
testb = 0.00001
limit = 1000

testa = 0.01
testb = 0.01
limit = 1000


tiger = (10,0,0,0)
for x in range(1,limit):
	low = int(x*0.2)+1
	hig = int(x*0.3)+1
	for y in range(low, hig):
		if y > x:
			break
		for z in range(low, hig):
			if z > y:
				break

			x /= math.sqrt(2)
			y /= math.sqrt(2)
			z /= math.sqrt(2)

			yx = y/x
			zx = z/x
			zy = z/y

			aa = abs(yx - ba)
			bb = abs(zx - ca)

			all = aa + bb
			if aa < testa and bb < testb:
				tiger = (all, aa, bb, x, y, z)
				print(tiger)

print("done")
#321 145 556
# 859 224 194
#487 127 110

#717 187 162
#602 157 136
#487 127 110