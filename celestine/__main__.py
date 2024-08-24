import PIL
import PIL.Image

a = 978900
b = 255310
c = 221105

ba = b / a # 0.2608131576
ca = c / a # 0.2258708754
cb = c / b # 0.8660256159

tiger = (10,0,0,0)

for x in range(1,1000):
	for y in range(1,1000):
		for z in range(1,1000):
			if z > y:
				continue

			if y > x:
				continue

			yx = y/x
			zx = z/x
			zy = z/y

			aa = abs(yx - ba)
			bb = abs(zx - ca)
			cc = abs(zy - cb)

			all = aa + bb + cc
			if all < tiger[0]:
				tiger = (all, x, y, z)

print(tiger)
print("done")
#321 145 556
# 859 224 194