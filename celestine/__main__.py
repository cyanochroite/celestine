""""""

import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])

celestine = __import__("celestine")
celestine.main(sys.argv[1:], True)

# pygame.display.update()
# pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
