from celestine import module

PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"


def python():
    try:
        python = module(PYTHON, PYTHON_3_6)
        python = module(PYTHON, PYTHON_3_7)
        python = module(PYTHON, PYTHON_3_8)
        python = module(PYTHON, PYTHON_3_9)
        python = module(PYTHON, PYTHON_3_10)
        python = module(PYTHON, PYTHON_3_11)
    except SyntaxError:
        pass
    return python