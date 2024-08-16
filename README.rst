Célestine
#########

.. image:: https://readthedocs.org/projects/celestine/badge/?version=latest
   :target: https://celestine.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://img.shields.io/github/repo-size/cyanochroite/celestine
   :alt: GitHub repo size
.. image:: https://img.shields.io/pypi/v/celestine
   :alt: PyPI - Version
   :target: https://pypi.org/project/celestine/
.. image:: https://img.shields.io/pypi/l/celestine
   :alt: PyPI - License
   :target: https://eupl.eu/
.. image:: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
   :alt: Calendar Versioning
   :target: https://calver.org/
.. image:: https://app.deepsource.com/gh/cyanochroite/celestine.svg/?label=active+issues&show_trend=false&token=1MUQkPi-6MM_PMqnaWrAJ6c7
  :target: https://app.deepsource.com/gh/cyanochroite/celestine/

A python framework for desktop applications.
Featuring support for multiple graphical user interfaces.
Localized for members of the European Union.


About
*****

The only requirement is Python.
However, you can install additional packages for extended functionality.

This has also been designed to run as a `Blender Add-on`_!
Note that Blender is an isolated environment, so other packages can not be used with it.


Project Update
^^^^^^^^^^^^^^

It seems that every release is broken in some form or another.
My plan of "just fix everything and then release it" has not been working out.
My new realization is that, since this is still in Alpha, it is okay that it is not perfect.
So I'm going to be releasing it "AS IS" for a while until Beta, where everything should be functioning as expected.
(The idea being that pushing out a semi-working package is better then leaving up a totaly broken package.)

Curently "pillow" and "platformdirs" are required dependencies because I have not made the workarounds yet.
Blender just dropped support for Python 3.10 and so I am going to be as well.
I would have liked to have a functioning Python 3.10 version so anyone who downloads this wont get errors, but it just hasn't happened yet.

In todays build, only pygame and tkinter are fully functional, using the "demo" and "viewer" applications.
(Unless there is another issue with the font file, then pygame wont work.)
Blender fails because it can't find the Pillow package, and it was having issues drawing images properly anyways.
Curses was having issues with windows-curses for a while, so I have not worked on it recently.
The DearPyGui Package seems to be nearly abandoned so I have not spent the time keeping it up to date.


Commands
********

Comand line arguments to use when launching the application.


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

+--------------+------------------------------+--------------+
| Interface    | Source                       | Command      |
+==============+==============================+==============+
| `blender`_   | Blender Foundation [1]_      | -i blender   |
+--------------+------------------------------+--------------+
| `curses`_    | Python Standard Library [2]_ | -i curses    |
+--------------+------------------------------+--------------+
| `dearpygui`_ | Python Package Index         | -i dearpygui |
+--------------+------------------------------+--------------+
| `pygame`_    | Python Package Index         | -i pygame    |
+--------------+------------------------------+--------------+
| `tkinter`_   | Python Standard Library [3]_ | -i tkinter   |
+--------------+------------------------------+--------------+


Natural Languages
^^^^^^^^^^^^^^^^^

+------------+------------------+---------+
| Language   | Translation [4]_ | Command |
+============+==================+=========+
| Bulgarian  | български        | -l bg   |
+------------+------------------+---------+
| Czech      | čeština          | -l cs   |
+------------+------------------+---------+
| Danish     | dansk            | -l da   |
+------------+------------------+---------+
| German     | Deutsch          | -l de   |
+------------+------------------+---------+
| Greek      | ελληνικά         | -l el   |
+------------+------------------+---------+
| English    | English          | -l en   |
+------------+------------------+---------+
| Spanish    | español          | -l es   |
+------------+------------------+---------+
| Estonian   | eesti            | -l et   |
+------------+------------------+---------+
| Finnish    | suomi            | -l fi   |
+------------+------------------+---------+
| French     | français         | -l fr   |
+------------+------------------+---------+
| Irish      | Gaeilge          | -l ga   |
+------------+------------------+---------+
| Croatian   | hrvatski         | -l hr   |
+------------+------------------+---------+
| Hungarian  | magyar           | -l hu   |
+------------+------------------+---------+
| Italian    | italiano         | -l it   |
+------------+------------------+---------+
| Lithuanian | lietuvių         | -l lt   |
+------------+------------------+---------+
| Latvian    | latviešu         | -l lv   |
+------------+------------------+---------+
| Maltese    | Malti            | -l mt   |
+------------+------------------+---------+
| Dutch      | Nederlands       | -l nl   |
+------------+------------------+---------+
| Polish     | polski           | -l pl   |
+------------+------------------+---------+
| Portuguese | português        | -l pt   |
+------------+------------------+---------+
| Romanian   | română           | -l ro   |
+------------+------------------+---------+
| Slovak     | slovenčina       | -l sk   |
+------------+------------------+---------+
| Slovenian  | slovenščina      | -l sl   |
+------------+------------------+---------+
| Swedish    | svenska          | -l sv   |
+------------+------------------+---------+


Optional Dependencies
*********************

+------------------------+---------------------------------------------------+
| Package                | Description                                       |
+========================+===================================================+
| `dearpygui`_           | DearPyGui: A simple Python GUI Toolkit            |
+------------------------+---------------------------------------------------+
| `pygame`_              | Python Game Development                           |
+------------------------+---------------------------------------------------+
| `windows-curses`_ [5]_ | Support for the standard curses module on Windows |
+------------------------+---------------------------------------------------+
| `pillow`_              | Python Imaging Library (Fork)                     |
+------------------------+---------------------------------------------------+


Funding
*******

The Célestine Project does not seek funding of any kind.
Any claims of fundraising activities in her name are fraudulent.
Please `contact me directly <celestine@cyanochroite.com>`_ if you encounter such claims.


Project Links
*************

* `Discord <https://discord.gg/aNmDWPXd7B>`_
* `Documentation <https://celestine.readthedocs.io/>`_
* `Email <celestine@cyanochroite.com>`_
* `Libraries.io <https://libraries.io/pypi/celestine>`_
* `PyPI <https://pypi.org/project/celestine/>`_
* `Source <https://github.com/cyanochroite/celestine>`_
* `Tracker <https://github.com/cyanochroite/celestine/issues>`_


Licences
********

The licence for :code:`Cascadia Code` is the
`SIL Open Font License <https://scripts.sil.org/OFL>`_.

The licence for :code:`celestine` is the
`European Union Public Licence <https://eupl.eu/>`_.


Footnotes
*********

.. [1] Blender interface can only be run when this is installed as a Blender addon.
.. [2] Windows does not come with Curses.
.. [3] Not always installed. Espically on Linix.
.. [4] Language files were translated from English using the Microsoft Azure Translator.
.. [5] Package only needed on Windows. Unix and Linix already have Curses.


.. _`dearpygui`: https://pypi.org/project/dearpygui/
.. _`pillow`: https://pypi.org/project/Pillow/
.. _`pygame`: https://pypi.org/project/pygame/
.. _`windows-curses`: https://pypi.org/project/windows-curses/

.. _`curses`: https://docs.python.org/3/library/curses.html
.. _`tkinter`: https://docs.python.org/3/library/tk.html

.. _`blender`: https://www.blender.org/
.. _`Blender Add-on`: https://docs.blender.org/manual/en/latest/editors/preferences/addons.html
