Wing Pro Preferences
####################

Code Warnings
*************

Configuration: Defaults
^^^^^^^^^^^^^^^^^^^^^^^

General
~~~~~~~

Show Import Not Found Warnings = True
Show Indent Warnings = True


Undefined Symbols
~~~~~~~~~~~~~~~~~

Show Undefined Name Warnings = True
Show Undefined Attribute Warnings = True


Unused Symbols
~~~~~~~~~~~~~~

Show Import Not Used Warnings = True
Show Variable Not Used Warnings = True
Show Argument Not Used Warnings = False
# False positive: "Argument not used." on "abc.abstractmethod".


Variables Not Used Configuration
""""""""""""""""""""""""""""""""

Always Show Globals Not Used in File = False
Show Extra Unpacked Variables Not Used = True
Use Regular Expressions to Identify Variables Intentionally Not Used = True


Values
''''''

_
cls
self
star


External Checkers
~~~~~~~~~~~~~~~~~

Enable External Checkers = True


External Code Checkers Configuration
""""""""""""""""""""""""""""""""""""


Flake8
''''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1000

Command Line = ${WING:PYTHON} -m flake8

Use Detected Indent Size = True

Use Configured Line Length = True


Mypy
''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1000

Command Line = ${WING:PYTHON} -m mypy --show-column-numbers


Pep8
''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1000

Command Line = ${WING:PYTHON} -m pycodestyle


Pylint
''''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1000

Command Line = ${WING:PYTHON} -m pylint --msg-template="{path}:{line}:{column}: {msg_id} {msg} ({symbol})" --ignored-argument-names="_|cls|hold|star|self"

Include Pylint Errors = True

Include Pylint Warnings = True

Include Pylint Info = True


Ruff
''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1000

Command Line = ${WING:PYTHON} -m ruff


Project Properties...
*********************

Python Path = A;B;C;D;E;F;

A = C:/Users/USER/FOLDER

B = C:/Program Files/Python312/Lib

C = C:/Program Files/Python312/DLLs

D = C:/Users/USER/AppData/Roaming/Python/Python312/site-packages

E = C:/Program Files/Python312

F = C:/Program Files/Python312/Lib/site-packages
