def yld123u(u):
    for i in range(1, 4):
        u = yield i * u


cat = range(1, 4)
print(list(cat))

gen = yld123u(4)
print(gen.send(None))
print(gen.send(3))
print(gen.send(5))
print(gen.send(6))
print(gen.send(7))

