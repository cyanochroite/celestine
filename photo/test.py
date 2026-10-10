array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def rat(iterable, length):
    for _ in range(length):
        yield next(iterable)


class Hat:

    def __init__(self, iterable, length):
        self.iterable = iterable
        self.length = length

    def __iter__(self):
        for _ in range(self.length):
            yield next(self.iterable)


def hats():
    snake = iter(array)
    width = 4
    height = 4

    for _ in range(height):
        iterable = rat(snake, width)
        yield tuple(iterable)


for car in hats():
    print(car)
    for bird in car:
        print(bird)
