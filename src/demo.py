cat = None
dog = None
fish = cat or dog
print(fish)
cow = [3]

print(cow[0])

import sys
applications = ["hi"]
try:
    final = sys.argv[1]
except IndexError:
    pass
else:
    if final not in applications:
        raise ValueError(applications)
