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
# test code used
python -m coverage run --source=celestine/application/unittest --module pytest --verbose

python -m coverage run --source=tests --module pytest --verbose
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
