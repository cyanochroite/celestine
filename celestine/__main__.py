""""""
import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])

celestine = __import__("celestine")
celestine.main(sys.argv[1:], True)


#Figure out how to recursivly call a package for all items in directory.
#Probably just find and copy how the others do it, with the best one.