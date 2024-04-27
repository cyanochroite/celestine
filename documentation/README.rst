.. image:: logo.png
   :align: center




.. role:: header-color

.. raw:: html

   <style>
   .header-color {
       align: center;
       background-color: MidnightBlue;
       color: #B2FFFF;
   }
   </style>

:header-color:`Célestine`
#########################


About
*****

A python framework for desktop applications.
Featuring support for multiple graphical user interfaces.
Localized for members of the European Union.

The only requirement is Python.
However, you can install additional packages for extended functionality.

This has also been designed to run as a `Blender Add-on`_!
Note that Blender is an isolated environment, so other packages can not be used with it.

.. _`Blender Add-on`: https://docs.blender.org/manual/en/latest/editors/preferences/addons.html



Commands
********

Applications
^^^^^^^^^^^^

Built in application to try out.

+-------------+-------------------------+------------------------------------------------------------------+
| Application | Command                 | Information                                                      |
+=============+=========================+==================================================================+
| Clean       | celestine -a clean      | Runs several code formatting  tools to get ready for publishing. |
+-------------+-------------------------+------------------------------------------------------------------+
| Demo        | celestine -a demo       | Test application for changing screens with buttons.              |
+-------------+-------------------------+------------------------------------------------------------------+
| Translator  | celestine -a translator | Translate the default language file into the 24 other languages. |
+-------------+-------------------------+------------------------------------------------------------------+
| Viewer      | celestine -a viewer     | Test application for viewing a limited number of images.         |
+-------------+-------------------------+------------------------------------------------------------------+

Caution: By default the viewer application will try to load every image it finds begining with the current working directory.


Graphical User Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+-------------------------+--------------+---------------------+
| Interface       | Source                  | celestine    | pip install         |
+=================+=========================+==============+=====================+
| `blender`_ [1]_ | Blender Foundation      | -i blender   |                     |
+-----------------+-------------------------+--------------+---------------------+
| `curses`_       | Python Standard Library | -i curses    | windows-curses [2]_ |
+-----------------+-------------------------+--------------+---------------------+
| `dearpygui`_    | Python Package Index    | -i dearpygui | dearpygui           |
+-----------------+-------------------------+--------------+---------------------+
| `pygame`_       | Python Package Index    | -i pygame    | pygame              |
+-----------------+-------------------------+--------------+---------------------+
| `tkinter`_      | Python Standard Library | -i tkinter   |                     |
+-----------------+-------------------------+--------------+---------------------+

Note:

.. [1] Blender interface can only be run when this is installed as a Blender addon.
.. [2] Package only needed on Windows. Unix and Linix already have Curses.

.. _`blender`: https://www.blender.org/
.. _`curses`: https://docs.python.org/3/howto/curses.html
.. _`dearpygui`: https://pypi.org/project/dearpygui/
.. _`pygame`: https://pypi.org/project/pygame/
.. _`pyupgrade`: https://pypi.org/project/pyupgrade/
.. _`tkinter`: https://docs.python.org/3/library/tk.html


Natural Languages
^^^^^^^^^^^^^^^^^

Languages translated from English using the Microsoft Azure Translator.

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
| `windows-curses`_ | windows-curses | Support for the standard curses module on Windows.                     |
+-------------------+----------------+------------------------------------------------------------------------+
| `Pillow`_         | Pillow         | Python Imaging Library (Fork)                                          |
+-------------------+----------------+------------------------------------------------------------------------+


.. _`dearpygui`: https://pypi.org/project/dearpygui/
.. _`pygame`: https://pypi.org/project/pygame/
.. _`windows-curses`: https://pypi.org/project/windows-curses/
.. _`Pillow`: https://pypi.org/project/Pillow/


Licences
********

The licence for :code:`Cascadia Code` is the
`SIL Open Font License <https://scripts.sil.org/OFL>`_.

The licence for :code:`celestine` is the
`European Union Public Licence <https://eupl.eu/>`_.


Project Links
*************

* `Discord <https://discord.gg/aNmDWPXd7B>`_
* `Documentation <https://celestine.readthedocs.io/>`_
* `Email <mem_dixy@pm.me>`_
* `Libraries.io <https://libraries.io/pypi/celestine>`_
* `PyPI <https://pypi.org/project/celestine/>`_
* `Source <https://github.com/mem-dixy/celestine>`_
* `Tracker <https://github.com/mem-dixy/celestine/issues>`_
