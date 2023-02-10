Célestine (Framework)
#####################

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

It has three customizable directories. ``application``, ``interface``, ``language``.
Any modules added to them should be automatically detected.

Comes with the application that started it all, a primitive image viewer.

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

Extensions
**********

If you are on Linux, you won’t have TKinter installed.
If you are on Windows, you won’t have curses installed.

For a better user experience, you may want to install these packages as well.

Note: Pygame has not yet been released for Python 3.11. Which is too bad because this currently does not run on Python 3.10.

+-------------------+----------------+------------------------------------------------------------------------+
| Package           | pip install    | Information                                                            |
+===================+================+========================================================================+
| `Dear PyGui`_     | dearpygui      | DearPyGui: A simple Python GUI Toolkit.                                |
+-------------------+----------------+------------------------------------------------------------------------+
| `Pygame`_         | pygame         | Python Game Development.                                               |
+-------------------+----------------+------------------------------------------------------------------------+
| `Windows Curses`_ | windows-curses | Support for the standard curses module on Windows.                     |
+-------------------+----------------+------------------------------------------------------------------------+

Commands
********

Application
^^^^^^^^^^^

Sample application to try out.

Caution: By default the viewer application will try to load every image it finds starting with the current working directory.

+-------------+-------------------------+------------------------------------------------------------------+
| Application | Command                 | Information                                                      |
+=============+=========================+==================================================================+
| Demo        | celestine -a demo       | Change screens with two whole buttons.                           |
+-------------+-------------------------+------------------------------------------------------------------+
| Translator  | celestine -a translator | Translate the default language file into the 24 other languages. |
+-------------+-------------------------+------------------------------------------------------------------+
| Viewer      | celestine -a viewer     | View a very small amount of pictures at once.                    |
+-------------+-------------------------+------------------------------------------------------------------+

Graphical User Interface
^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+-------------------------+------------------------+
| Interface     | Type                    | Command                |
+===============+=========================+========================+
| `Blender`_    | Application             | celestine -i blender   |
+---------------+-------------------------+------------------------+
| `Curses`_     | Python Standard Library | celestine -i curses    |
+---------------+-------------------------+------------------------+
| `Dear PyGui`_ | Python Package Index    | celestine -i dearpygui |
+---------------+-------------------------+------------------------+
| `Pygame`_     | Python Package Index    | celestine -i pygame    |
+---------------+-------------------------+------------------------+
| `Tkinter`_    | Python Standard Library | celestine -i tkinter   |
+---------------+-------------------------+------------------------+

World Language
^^^^^^^^^^^^^^

+------------+-------------+-----------------+
| Language   | Translation | Command         |
+============+=============+=================+
| Bulgarian  | български   | celestine -l en |
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

Resources
*********

* `Email`_
* `Discord`_
* `Read the Docs`_

.. _`Blender`: https://www.blender.org/
.. _`Celestine`: https://pypi.org/project/celestine/
.. _`Curses`: https://docs.python.org/3/howto/curses.html
.. _`Dear PyGui`: https://github.com/hoffstadt/DearPyGui/
.. _`Discord`: https://discord.gg/aNmDWPXd7B
.. _`Email`: celestine@mem-dixy.ch
.. _`Python`: https://www.python.org/
.. _`Pygame`: https://www.pygame.org/
.. _`Read the Docs`: https://celestine.readthedocs.io/en/latest/
.. _`Tkinter`: https://docs.python.org/3/library/tk.html
.. _`Windows Curses`: https://github.com/zephyrproject-rtos/windows-curses/



