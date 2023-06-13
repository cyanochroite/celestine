celestine
#########

.. image:: https://readthedocs.org/projects/celestine/badge/?version=latest
   :target: https://celestine.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

About
*****
A python framework for desktop applications.
Featuring support for multiple graphical user interfaces.
Localized for members of the European Union.

The only requirement is Python.
However, you can install additional packages for extended functionality.

Installation
************

Celestine
^^^^^^^^^

Python Package Index
~~~~~~~~~~~~~~~~~~~~

Install from pip::

    pip install celestine

GitHub
~~~~~~

https://github.com/mem-dixy/celestine

Python
^^^^^^

`Python`_ >= 3.10
~~~~~~~~~~~~~~~~~

The recommended option. Or you can install Blender instead.

Currently supports Python 3.10 to Python 3.11.

`Blender`_
~~~~~~~~~~

Or you can install Python instead.

Blender comes with a python interpreter, which means this can be run as a blender add-on.
(It used to work anyways. Doing anything in Blender is hard, so upkeep has fallen behind.)

Note that Blender is an isolated environment, so no other packages can be used with it.



Commands
********

Applications
^^^^^^^^^^^^

Sample application to try out.

Caution: By default the viewer application will try to load every image it finds begining with the current working directory.

+-------------+-------------------------+------------------------------------------------------------------+
| Application | Command                 | Information                                                      |
+=============+=========================+==================================================================+
| Demo        | celestine -a demo       | Change screens with two whole buttons.                           |
+-------------+-------------------------+------------------------------------------------------------------+
| Translator  | celestine -a translator | Translate the default language file into the 24 other languages. |
+-------------+-------------------------+------------------------------------------------------------------+
| Viewer      | celestine -a viewer     | View a very small amount of pictures at once.                    |
+-------------+-------------------------+------------------------------------------------------------------+


Graphical User Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+-------------------------+------------------------+
| Interface    | Source                  | Command                |
+==============+=========================+========================+
| `blender`_   | Blender Foundation      | celestine -i blender   |
+--------------+-------------------------+------------------------+
| `curses`_    | Python Standard Library | celestine -i curses    |
+--------------+-------------------------+------------------------+
| `dearpygui`_ | Python Package Index    | celestine -i dearpygui |
+--------------+-------------------------+------------------------+
| `pygame`_    | Python Package Index    | celestine -i pygame    |
+--------------+-------------------------+------------------------+
| `tkinter`_   | Python Standard Library | celestine -i tkinter   |
+--------------+-------------------------+------------------------+

+--------------+-------------------------+--------------+-----------------------------+
| Interface    | Source                  | celestine -i | pip install                 |
+==============+=========================+==============+=============================+
| `blender`_   | Blender Foundation      | blender      | dearpygui                   |
+--------------+-------------------------+--------------+-----------------------------+
| `curses`_    | Python Standard Library | curses       | windows-curses [1]_         |
+--------------+-------------------------+--------------+-----------------------------+
| `dearpygui`_ | Python Package Index    | dearpygui    | dearpygui                   |
+--------------+-------------------------+--------------+-----------------------------+
| `pygame`_    | Python Package Index    | pygame       | pygame                      |
+--------------+-------------------------+--------------+-----------------------------+
| `tkinter`_   | Python Standard Library | tkinter      | tkinter                     |
+--------------+-------------------------+--------------+-----------------------------+


Note:

.. [1] This is only needed on Windows.





.. _`blender`: https://www.blender.org/
.. _`curses`: https://docs.python.org/3/howto/curses.html
.. _`dearpygui`: https://pypi.org/project/dearpygui/
.. _`pygame`: https://pypi.org/project/pygame/
.. _`pyupgrade`: https://pypi.org/project/pyupgrade/
.. _`tkinter`: https://docs.python.org/3/library/tk.html


World Languages
^^^^^^^^^^^^^^^

+------------+-------------+-----------------+
| Language   | Translation | Command         |
+============+=============+=================+
| Bulgarian  | български   | celestine -l bg |
+------------+-------------+-----------------+
| Czech      | čeština     | celestine -l cs |
+------------+-------------+-----------------+
| Danish     | dansk       | celestine -l da |
+------------+-------------+-----------------+
| German     | Deutsch     | celestine -l de |
+------------+-------------+-----------------+
| Greek      | ελληνικά    | celestine -l el |
+------------+-------------+-----------------+
| English    | English     | celestine -l en |
+------------+-------------+-----------------+
| Spanish    | español     | celestine -l es |
+------------+-------------+-----------------+
| Estonian   | eesti       | celestine -l et |
+------------+-------------+-----------------+
| Finnish    | suomi       | celestine -l fi |
+------------+-------------+-----------------+
| French     | français    | celestine -l fr |
+------------+-------------+-----------------+
| Irish      | Gaeilge     | celestine -l ga |
+------------+-------------+-----------------+
| Croatian   | hrvatski    | celestine -l hr |
+------------+-------------+-----------------+
| Hungarian  | magyar      | celestine -l hu |
+------------+-------------+-----------------+
| Italian    | italiano    | celestine -l it |
+------------+-------------+-----------------+
| Lithuanian | lietuvių    | celestine -l lt |
+------------+-------------+-----------------+
| Latvian    | latviešu    | celestine -l lv |
+------------+-------------+-----------------+
| Maltese    | Malti       | celestine -l mt |
+------------+-------------+-----------------+
| Dutch      | Nederlands  | celestine -l nl |
+------------+-------------+-----------------+
| Polish     | polski      | celestine -l pl |
+------------+-------------+-----------------+
| Portuguese | português   | celestine -l pt |
+------------+-------------+-----------------+
| Romanian   | română      | celestine -l ro |
+------------+-------------+-----------------+
| Slovak     | slovenčina  | celestine -l sk |
+------------+-------------+-----------------+
| Slovenian  | slovenščina | celestine -l sl |
+------------+-------------+-----------------+
| Swedish    | svenska     | celestine -l sv |
+------------+-------------+-----------------+


Optional Dependencies
*********************

+-------------------+----------------+------------------------------------------------------------------------+
| Package           | pip install    | Information                                                            |
+===================+================+========================================================================+
| `dearpygui`_      | dearpygui      | DearPyGui: A simple Python GUI Toolkit.                                |
+-------------------+----------------+------------------------------------------------------------------------+
| `pygame`_         | pygame         | Python Game Development.                                               |
+-------------------+----------------+------------------------------------------------------------------------+


Windows
^^^^^^^

+-------------------+----------------+------------------------------------------------------------------------+
| Package           | pip install    | Information                                                            |
+===================+================+========================================================================+
| `windows-curses`_ | windows-curses | Support for the standard curses module on Windows.                     |
+-------------------+----------------+------------------------------------------------------------------------+


.. _`dearpygui`: https://pypi.org/project/dearpygui/
.. _`pygame`: https://pypi.org/project/pygame/
.. _`windows-curses`: https://github.com/zephyrproject-rtos/windows-curses/


Licences
********

The licence for :program:`Cascadia Code` is the
`SIL Open Font License <https://scripts.sil.org/OFL>`_.

The licence for :program:`celestine` is the
`European Union Public Licence <https://eupl.eu/>`_.


Project Links
*************

* `Discord <https://discord.gg/aNmDWPXd7B>`_
* `Documentation <https://celestine.readthedocs.io/>`_
* `Email <celestine@mem-dixy.ch>`_
* `PyPI <https://pypi.org/project/celestine/>`_
* `Source <https://github.com/mem-dixy/celestine>`_
* `Tracker <https://github.com/mem-dixy/celestine/issues>`_
