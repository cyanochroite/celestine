Dependencies
############

Distribution
************

build
^^^^^
python -m build


twine
^^^^^

python -m twine check --strict dist/*

# test
python -m twine upload --verbose --repository testpypi dist/*

# real
python -m twine upload --verbose dist/*


validation
**********

sphinx
^^^^^^
python -m sphinx documentation doc


validation
**********

black
^^^^^
python -m black celestine
pyproject.toml
https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file


coverage
^^^^^^^^
python -m coverage run --source=celestine --module pytest --verbose
python -m coverage report --show-missing
python -m coverage html

# test code used
python -m coverage run --source=celestine/application/tests --module pytest --verbose

python -m coverage run --source=celestine/tests --module pytest --verbose
python -m coverage report --show-missing
python -m coverage html

# source code used by test code
python -m coverage run --module pytest --verbose celestine/application/unittest
python -m coverage report --show-missing
python -m coverage html

# source code used
python -m coverage run --source=celestine --module pytest --verbose celestine/application/unittest
python -m coverage report --show-missing
python -m coverage html

setup.cfg
https://coverage.readthedocs.io/en/7.2.0/config.html#configuration-reference


flake8
^^^^^^
python -m flake8 celestine
setup.cfg
https://flake8.pycqa.org/en/latest/user/configuration.html#configuring-flake8


isort
^^^^^
python -m isort celestine
pyproject.toml
https://pycqa.github.io/isort/docs/configuration/options.html

mypy
^^^^
python -m mypy celestine
setup.cfg
https://mypy.readthedocs.io/en/stable/config_file.html#config-file-format


pycodestyle
^^^^^^^^^^^
python -m pycodestyle celestine
setup.cfg
https://pycodestyle.pycqa.org/en/latest/intro.html#configuration


pylint
^^^^^^
python -m pylint celestine
pyproject.toml
https://pylint.pycqa.org/en/latest/user_guide/configuration/all-options.html#standard-checkers


pyright
^^^^^^^
python -m pyright celestine
pyproject.toml
https://github.com/microsoft/pyright/blob/main/docs/configuration.md#pyright-configuration








Package Dependency
^^^^^^^^^^^^^^^^^^


* `autoflake`_ :command:`pip install autoflake`
* `black`_ :command:`pip install black`
* `isort`_ :command:`pip install isort`
* `pydocstringformatter`_ :command:`pip install pydocstringformatter`
* `pygame`_ :command:`pip install pygame`
* `pyupgrade`_ :command:`pip install pyupgrade`


.. _`autoflake`: https://pypi.org/project/autoflake/
.. _`black`: https://pypi.org/project/black/
.. _`isort`: https://pypi.org/project/isort/
.. _`pydocstringformatter`: https://www.python.org/
.. _`pygame`: https://pypi.org/project/pygame/
.. _`pyupgrade`: https://pypi.org/project/pyupgrade/


Package Dependency
^^^^^^^^^^^^^^^^^^


Notes:
1. On Windows, use 'pip install windows-curses'.


.. _`autoflake`: https://pypi.org/project/autoflake/
.. _`black`: https://pypi.org/project/black/
.. _`curses`: https://docs.python.org/3/howto/curses.html
.. _`dearpygui`: https://pypi.org/project/dearpygui/
.. _`isort`: https://pypi.org/project/isort/
.. _`pydocstringformatter`: https://www.python.org/
.. _`pygame`: https://pypi.org/project/pygame/
.. _`pyupgrade`: https://pypi.org/project/pyupgrade/
.. _`tkinter`: https://docs.python.org/3/library/tk.html
