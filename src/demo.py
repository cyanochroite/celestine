from celestine.data.version import Version

car = Version("3.10")
cat = Version("3.21.1")
print(car<cat)

bat = Version()
print(bat)

candy = ".".split(".")
print(candy)


(major, minor, patch, *ignore) = ".0.0".split(".")
print(major, minor, patch)


car = 2
print(car)
cat = car << 8
print(cat)


#from celestine.extension.more_itertools import more_itertools
#more_itertools.first_true([1])

import celestine.extension.Python37 as hi
import celestine.extension.Python_38
import celestine.extension.Python_3_9
import celestine.extension.Python3_10
