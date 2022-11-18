"""
Class to help represent and _compare different version numbers.

See https://semver.org/ for more details.
"""


class Version():
    """
    Class to help represent and _compare different version numbers.

    See https://semver.org/ for more details.
    """

    def __bool__(self):
        return self.major > 0 or self.minor > 0 or self.patch > 0

    def __eq__(self, other):
        return self._compare() == other._compare()

    def __ge__(self, other):
        return self._compare() >= other._compare()

    def __gt__(self, other):
        return self._compare() > other._compare()

    def __hash__(self):
        return hash((self.major, self.minor, self.patch))

    def __init__(self, version="0"):
        version += ".0.0"
        (major, minor, patch, *_) = version.split(".")
        self.major = abs(int(major))
        self.minor = abs(int(minor))
        self.patch = abs(int(patch))

    def __le__(self, other):
        return self._compare() <= other._compare()

    def __lt__(self, other):
        return self._compare() < other._compare()

    def __ne__(self, other):
        return self._compare() != other._compare()

    def __repr__(self):
        return F"Version({self.major}, {self.minor}, {self.patch})"

    def __str__(self):
        return F"{self.major}.{self.minor}.{self.patch}"

    def _compare(self):
        number = 0
        number += self.major
        number <<= 8
        number += self.minor
        number <<= 8
        number += self.patch
        number <<= 8
        return number
