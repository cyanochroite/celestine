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


shorter1 = 1 / math.sqrt(2)
double1 = math.sqrt(2)
oval1 = math.sqrt(2) / math.sqrt(3)


elipse1 = shorter1 / math.sqrt(3)
longer1 = shorter1 * math.pi * math.sqrt(2)
dimond1 = longer1 + double1 + elipse1

lowest =  1.0 / 65536 * 1000
lowest =  1


maxlen = (2048 / 2) / math.sqrt(2)
print(maxlen)

def fix(numer):
	return abs(round(numer) - numer)

for index in range(110,170):
	shorter = index * shorter1
	double = index * double1
	elipse = index * elipse1
	oval = index * oval1
	longer = index * longer1
	dimond = index * dimond1 + index
	longer = 1
	dimond = 1

	a = fix(index)
	b = fix(shorter)
	c = fix(elipse)
	d = fix(oval)
	e = fix(longer)
	f = fix(dimond)
	g = fix(double)

	a1 = round(index)
	b1 = round(shorter)
	c1 = round(elipse)
	d1 = round(oval)
	e1 = round(longer)
	f1 = round(dimond)
	g1 = round(double)

	z = a+b+c+d+e+f+g
	z = b+d
#	if a < lowest and b<lowest and c<lowest:
	if z < lowest:
		print(f"{index}\t{b}\t{b1}\t{d}\t{d1}\t{z}")
		#print(f"{index}\t{a}\t{b}\t{c}\t{d}\t{e}\t{f}\t{g}\t{z}")
		#print(f"{a1}\t{b1}\t{c1}\t{d1}\t{e1}\t{f1}\t{g1}\t<<")

limit = 0
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