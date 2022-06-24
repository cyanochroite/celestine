"""Class to help represent and compare different version numbers."""
# https://semver.org/


class Version():
    def __bool__(self):
        return self.major > 0 or self.minor > 0 or self.patch > 0

    def __eq__(self, other):
        if self.major < other.major:
            return False

        if self.major > other.major:
            return False

        if self.minor < other.minor:
            return False

        if self.minor > other.minor:
            return False

        if self.patch < other.patch:
            return False

        if self.patch > other.patch:
            return False

        return True

    def __ge__(self, other):
        if self.major < other.major:
            return False

        if self.major > other.major:
            return True

        if self.minor < other.minor:
            return False

        if self.minor > other.minor:
            return True

        if self.patch < other.patch:
            return False

        if self.patch > other.patch:
            return True

        return True

    def __gt__(self, other):
        if self.major < other.major:
            return False

        if self.major > other.major:
            return True

        if self.minor < other.minor:
            return False

        if self.minor > other.minor:
            return True

        if self.patch < other.patch:
            return False

        if self.patch > other.patch:
            return True

        return False

    def __hash__(self):
        return hash((self.major, self.minor, self.patch))

    def __init__(self, version="0"):
        version += ".0.0"
        (major, minor, patch, *ignore) = version.split(".")
        self.major = abs(int(major))
        self.minor = abs(int(minor))
        self.patch = abs(int(patch))

    def __le__(self, other):
        if self.major < other.major:
            return True

        if self.major > other.major:
            return False

        if self.minor < other.minor:
            return True

        if self.minor > other.minor:
            return False

        if self.patch < other.patch:
            return True

        if self.patch > other.patch:
            return False

        return True

    def __lt__(self, other):
        if self.major < other.major:
            return True

        if self.major > other.major:
            return False

        if self.minor < other.minor:
            return True

        if self.minor > other.minor:
            return False

        if self.patch < other.patch:
            return True

        if self.patch > other.patch:
            return False

        return False

    def __ne__(self, other):
        if self.major < other.major:
            return True

        if self.major > other.major:
            return True

        if self.minor < other.minor:
            return True

        if self.minor > other.minor:
            return True

        if self.patch < other.patch:
            return True

        if self.patch > other.patch:
            return True

        return False

    def __repr__(self):
        return "Version({0}, {1}, {2})".format(self.major, self.minor, self.patch)

    def __str__(self):
        return "{0}.{1}.{2}".format(self.major, self.minor, self.patch)
