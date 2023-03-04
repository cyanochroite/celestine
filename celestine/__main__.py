""""""

import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])

__import__("celestine").main(sys.argv[1:], True)


# coverage

# pylint
# pyright

# flake8
# mypy
