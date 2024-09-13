"""
A = 4356
B = 2178
C = 751
D = 681
E = 478
F = 338
G = 276
H = 239
J = 198
K = 140
L = 99
M = 70
"""

import math


def fix(numer: float) -> float:
    """"""
    return abs(round(numer) - numer)


def find(a: float, b: float, c: float, d: float, limit: int) -> float:
    """"""

    result = 0.0
    lowest = 2.0
    for index in range(1, limit):
        number = index * math.sqrt(2)

        one = number / a
        two = number / b
        tri = number / c
        tet = number / d

        error = fix(one) + fix(two) + fix(tri) + fix(tet)

        one = round(one)
        two = round(two)
        tri = round(tri)
        tet = round(tet)

        if error < lowest:
            lowest = error
            result = number
            print(f"{one}\t{two}\t{tri}\t{tet}\t{error}")

    return result


def show(number: float) -> int:
    """"""
    result = round(number)
    print(result)
    return result


print("start")
X = find(math.sqrt(1), math.sqrt(2), math.sqrt(3), math.sqrt(4), 3000)
print("next")
Y = find(math.sqrt(1), math.sqrt(2), math.sqrt(4), math.sqrt(8), 300)
print("done")


E = show(X / math.sqrt(1))
F = show(X / math.sqrt(2))
G = show(X / math.sqrt(3))
H = show(X / math.sqrt(4))

J = show(Y / math.sqrt(1))
K = show(Y / math.sqrt(2))
L = show(Y / math.sqrt(4))
M = show(Y / math.sqrt(8))

C = show(H * math.pi)
D = show(C - M)
B = show(F + K + D + J + D + K)
A = show(B * 2)
