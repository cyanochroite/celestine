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
Show Argument Not Used Warnings = True


Variables Not Used Configuration
""""""""""""""""""""""""""""""""

Always Show Globals Not Used in File = True
Show Extra Unpacked Variables Not Used = True
Use Regular Expressions to Identify Variables Intentionally Not Used = True


Values
''''''

_
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

Maximum File Size (KB) = 500

Command Line = ${WING:PYTHON} -m flake8 --indent-size=4 --max-line-length=72

Use Detected Indent Size = True

Use Configured Line Length = True


Mypy
''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 500

Command Line = ${WING:PYTHON} -m mypy --show-column-numbers


Pep8
''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 500

Command Line = ${WING:PYTHON} -m pycodestyle


Pylint
''''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 500

Command Line = ${WING:PYTHON} -m pylint "--msg-template={path}:{line}:{column}: {msg_id} {msg} ({symbol})" --ignored-argument-names=_|star

Include Pylint Errors = True

Include Pylint Warnings = True

Include Pylint Info = True


Ruff
''''

Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 500

Command Line = ${WING:PYTHON} -m ruff check


Advanced Configuration
""""""""""""""""""""""

Show Warnings in the Standard Library = True

Show Warnings in site-packages = True

Allow Comments to Disable Warnings = True


Project Properties...
*********************

Environment
^^^^^^^^^^^

Python Executable
~~~~~~~~~~~~~~~~~

Command Line = True
Path = /home/mem_dixy/applications/python/python

Python Path = A:B:C:D:E:F

A = /run/media/system/data/celestine

B = /home/linuxbrew/.linuxbrew/lib/python3.14

C = /home/linuxbrew/.linuxbrew/lib/python3.14/lib-dynload

D = /home/mem_dixy/applications/python/lib/python3.14/site-packages

E = /home/linuxbrew/.linuxbrew/opt/python-tk@3.14/libexec
