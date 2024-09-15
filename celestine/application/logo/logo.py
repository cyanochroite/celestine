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


def main(limit: int) -> None:
    """"""
    lowest = 4.0
    for index in range(7, limit):
        major = index * math.sqrt(2)
        minor = major / (1 + math.sqrt(2))

        one = [
            major / math.sqrt(1),
            major / math.sqrt(2),
            major / math.sqrt(3),
            major / math.sqrt(4),
            minor / math.sqrt(1),
            minor / math.sqrt(2),
            minor / math.sqrt(4),
            minor / math.sqrt(8),
        ]
        error = sum(map(fix, one))
        one = list(map(round, one))

        two: list[float] = []
        two.append(one[3] * math.pi)
        two.append(two[0] - one[7])
        two.append(one[1] + one[5] + two[1] + one[4] + two[1] + one[5])
        two.append(round(two[2]) * 2)
        two = list(map(round, two))

        if error < lowest:
            lowest = error
            number = [*one, *two]
            number.sort()
            print(error, index, number)


if __name__ == "__main__":
    main(3500)
