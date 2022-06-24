from celestine.data.version import Version

car = Version("3.10")
cat = Version("3.1.1")
print(car<cat)

bat = Version()
print(bat)

candy = ".".split(".")
print(candy)


(major, minor, patch, *ignore) = ".0.0".split(".")
print(major, minor, patch)