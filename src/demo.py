import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

from celestine.core import load
from celestine.core.file import File



module = load.module("application", "language", "keyword")
dictionary = load.dictionary(module)
dog = list(dictionary)
dog.sort()
car = map(lambda a: (a, str(dictionary[a])), dog)
candy = list(car)
cat = File("test", "none", candy)
cat.save(directory)

