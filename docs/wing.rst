Wing Pro Preferences
####################

Code Warnings
*************

Configuration Defaults
^^^^^^^^^^^^^^^^^^^^^^

External Checkers
~~~~~~~~~~~~~~~~~

External Code Checkers Configuration
""""""""""""""""""""""""""""""""""""

Flake8
''''''
Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1500

Command Line = ${WING:PYTHON} -m flake8

Use Detected Indent Size = True

Use Configured Line Length = True

Mypy
''''
Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1500

Command Line = ${WING:PYTHON} -m mypy --show-column-numbers

Pep8
''''
Enabled = True

Run after save = True

Run after opening file = True

Maximum File Size (KB) = 1500

Command Line = ${WING:PYTHON} -m pycodestyle


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

A = C:/Users/ADMIN/AppData/Local/Programs/Python/Python310/DLLs

B = C:/Users/ADMIN/AppData/Local/Programs/Python/Python310/Lib

C = C:/Users/ADMIN/AppData/Local/Programs/Python/Python310/Lib/site-packages

D = C:/Users/ADMIN/celestine/source
