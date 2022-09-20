from celestine.core import load

from celestine.keyword.all import PYTHON
from celestine.keyword.all import PYTHON_3_6
from celestine.keyword.all import PYTHON_3_7
from celestine.keyword.all import PYTHON_3_8
from celestine.keyword.all import PYTHON_3_9
from celestine.keyword.all import PYTHON_3_10
from celestine.keyword.all import PYTHON_3_11


def version():
    try:
        python = load.module(PYTHON, PYTHON_3_6)
        python = load.module(PYTHON, PYTHON_3_7)
        python = load.module(PYTHON, PYTHON_3_8)
        python = load.module(PYTHON, PYTHON_3_9)
        python = load.module(PYTHON, PYTHON_3_10)
        python = load.module(PYTHON, PYTHON_3_11)
    except SyntaxError:
        pass
    return python
