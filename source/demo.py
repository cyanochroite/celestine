def yld123u(u):
    for i in range(1, 4):
        received = yield i * u  # a sent value will be assigned to 'received'
        u = u if received is None else received


for x in yld123u(4):
    print(x)

gen = yld123u(4)
v0 = next(gen)
v1 = next(gen)
v2 = gen.send(4)
v = gen.send(4)
gen.close()
v2 = gen.send(4)
print(v0, v1, v2)

if None:
    print(1)
if '':
    print(2)
if ' ':
    print(3)
