import os.path
from celestine.data.unicode import FULL_STOP


APPLICATION = "celestine"



def file(session, iterable):
    root = session["Application"]["directory"]
    carwash = [root, APPLICATION] + iterable
    return os.path.join(*tuple(carwash))
#return os.path.join([root, APPLICATION] + iterable)

def import_module(*paths):
    iterable = [APPLICATION] + list(paths)
    name = FULL_STOP.join(iterable)
    module =  __import__(name)
    for path in paths:
        module = getattr(module, path)
    return module
