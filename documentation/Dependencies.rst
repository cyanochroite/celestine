Wing Pro Preferences
####################

Code Warnings
*************

Configuration Defaults
^^^^^^^^^^^^^^^^^^^^^^

Unused Symbols
~~~~~~~~~~~~~~

Variables Not Used Configuration
""""""""""""""""""""""""""""""""
Always Show Globals Not Used in File = False
Show Extra Unpacked Variables Not Used
Use Regular Expressions to Identify Variables Intentionally Not Used = True
Values = ["_"]

External Checkers
~~~~~~~~~~~~~~~~~

External Code Checkers Configuration
""""""""""""""""""""""""""""""""""""

Flake8 black
''''''
python -m black celestine --line-length 72


Flake8
''''''
python -m flake8 celestine


Mypy
''''
python -m mypy celestine
redo

pycodestyle
''''
python -m pycodestyle celestine


Pylint
''''''
Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1500

Command Line = ${WING:PYTHON} -m pylint --msg-template="{path}:{line}:{column}: {msg_id} {msg} ({symbol})"

Include Pylint Errors = True

Include Pylint Warnings = True

Include Pylint Info = True

Project Properties
******************
Python Path = A;B;C;D

A = C:/Users/USER/AppData/Local/Programs/Python/Python310/DLLs

B = C:/Users/USER/AppData/Local/Programs/Python/Python310/Lib

C = C:/Users/USER/AppData/Local/Programs/Python/Python310/Lib/site-packages

D = C:/Users/USER/celestine/source
