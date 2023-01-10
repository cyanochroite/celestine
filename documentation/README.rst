The Celestine Image Viewer
##########################

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    note
    wing

- About_
- Requirements_
- Inspiration_
- Info_

.. _About:

About
*****
View, tag, and organize your photos. Well, that was the origional goal.
This started out as a simple image viewer, and in a way it still is.
I wanted this to work with a variety of languges and GUIs, which required a lot of work.
At this point it is now a minature framework for desktop applications.

Custom Install
^^^^^^^^^^^^^^
Choose which packages to use.

Swap packages

- Has no required dependencies. (All you need to run this package is Python.)
- Can be customized to use different packages. (See the list below for supported packages.)

Secondary goals:
- Advanced tag searching. (Most websites have really lousy topic filters.)

What this is not:
- This is not a photo editor.
- This is not a photo downloader.
- This is not a mobile application.

Requirements
************

The Python Programming Language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently supporting Python 3.11 (Used to support Python 3.10)

This is a Python application, and so it needs Python in order to run.
Don't feel like installing Python? Try running it in Blender insead!
(Blender support comming soon.)

Application
^^^^^^^^^^^

If you want celestine to be more then just a command line tool, you will need at least one of these installed:
(Pygame has not yet been released for Python 3.11.) (Blender is hard so it has fallen behind in upkeep.)

+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| Interface         | Type                    | How                                                    | Information                                                            |
+===================+=========================+========================================================+========================================================================+
| `Blender`_        | Application             | Install celestine as a Blender Add-on                  | Secondary scripts, called Add-ons, that extends Blender functionality. |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Curses`_         | Python Standard Library | Python Installer                                       | The Windows version of Python does not include the curses module.      |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Dear PyGui`_     | Python Package Index    | pip install dearpygui                                  | DearPyGui: A simple Python GUI Toolkit.                                |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Pygame`_         | Python Package Index    | pip install pygame                                     | Python Game Development.                                               |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Tkinter`_        | Python Standard Library | Python Installer > Optional Features > tcl/tk and IDLE | The tkinter package is a thin object-oriented layer on top of Tcl/Tk.  |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Windows Curses`_ | Python Package Index    | pip install windows-curses                             | Support for the standard curses module on Windows.                     |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+

Interface
^^^^^^^^^

If you want celestine to be more then just a command line tool, you will need at least one of these installed:
(Pygame has not yet been released for Python 3.11.) (Blender is hard so it has fallen behind in upkeep.)

+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| Interface         | Type                    | How                                                    | Information                                                            |
+===================+=========================+========================================================+========================================================================+
| `Blender`_        | Application             | Install celestine as a Blender Add-on                  | Secondary scripts, called Add-ons, that extends Blender functionality. |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Curses`_         | Python Standard Library | Python Installer                                       | The Windows version of Python does not include the curses module.      |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Dear PyGui`_     | Python Package Index    | pip install dearpygui                                  | DearPyGui: A simple Python GUI Toolkit.                                |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Pygame`_         | Python Package Index    | pip install pygame                                     | Python Game Development.                                               |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Tkinter`_        | Python Standard Library | Python Installer > Optional Features > tcl/tk and IDLE | The tkinter package is a thin object-oriented layer on top of Tcl/Tk.  |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+
| `Windows Curses`_ | Python Package Index    | pip install windows-curses                             | Support for the standard curses module on Windows.                     |
+-------------------+-------------------------+--------------------------------------------------------+------------------------------------------------------------------------+

Languages
^^^^^^^^^
The EU is characterised by its cultural and linguistic diversity, and the languages spoken in EU countries are an essential part of its cultural heritage. This is why the EU supports multilingualism in its programmes and in the work of its institutions.

The EU has 24 official languages:

Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish and Swedish.


+----+------------+-------------+--------------------+
|    | Language   | Translation | ISO 3166-1 alpha-2 |
+====+============+=============+====================+
| bg | Bulgarian  | български   | celestine -l en    |
+----+------------+-------------+--------------------+
| cs | Czech      | čeština     | celestine -l cs    |
+----+------------+-------------+--------------------+
| da | Danish     | dansk       | celestine -l da    |
+----+------------+-------------+--------------------+
| de | German     | Deutsch     | celestine -l de    |
+----+------------+-------------+--------------------+
| el | Greek      | ελληνικά    | celestine -l el    |
+----+------------+-------------+--------------------+
| en | English    | English     | celestine -l en    |
+----+------------+-------------+--------------------+
| es | Spanish    | español     | celestine -l es    |
+----+------------+-------------+--------------------+
| et | Estonian   | eesti       | celestine -l et    |
+----+------------+-------------+--------------------+
| fi | Finnish    | suomi       | celestine -l fi    |
+----+------------+-------------+--------------------+
| fr | French     | français    | celestine -l fr    |
+----+------------+-------------+--------------------+
| ga | Irish      | Gaeilge     | celestine -l ga    |
+----+------------+-------------+--------------------+
| hr | Croatian   | hrvatski    | celestine -l hr    |
+----+------------+-------------+--------------------+
| hu | Hungarian  | magyar      | celestine -l hu    |
+----+------------+-------------+--------------------+
| it | Italian    | italiano    | celestine -l it    |
+----+------------+-------------+--------------------+
| lt | Lithuanian | lietuvių    | celestine -l lt    |
+----+------------+-------------+--------------------+
| lv | Latvian    | latviešu    | celestine -l lv    |
+----+------------+-------------+--------------------+
| mt | Maltese    | Malti       | celestine -l mt    |
+----+------------+-------------+--------------------+
| nl | Dutch      | Nederlands  | celestine -l nl    |
+----+------------+-------------+--------------------+
| pl | Polish     | polski      | celestine -l pl    |
+----+------------+-------------+--------------------+
| pt | Portuguese | português   | celestine -l pt    |
+----+------------+-------------+--------------------+
| ro | Romanian   | română      | celestine -l ro    |
+----+------------+-------------+--------------------+
| sk | Slovak     | slovenčina  | celestine -l sk    |
+----+------------+-------------+--------------------+
| sl | Slovenian  | slovenščina | celestine -l sl    |
+----+------------+-------------+--------------------+
| sv | Swedish    | svenska     | celestine -l sv    |
+----+------------+-------------+--------------------+


+------------+-------------+--------------------+
| Language   | Translation | ISO 3166-1 alpha-2 |
+============+=============+====================+
| Bulgarian  | български   | celestine -l en    |
+------------+-------------+--------------------+
| Czech      | čeština     | celestine -l cs    |
+------------+-------------+--------------------+
| Danish     | dansk       | celestine -l da    |
+------------+-------------+--------------------+
| German     | Deutsch     | celestine -l de    |
+------------+-------------+--------------------+
| Greek      | ελληνικά    | celestine -l el    |
+------------+-------------+--------------------+
| English    | English     | celestine -l en    |
+------------+-------------+--------------------+
| Spanish    | español     | celestine -l es    |
+------------+-------------+--------------------+
| Estonian   | eesti       | celestine -l et    |
+------------+-------------+--------------------+
| Finnish    | suomi       | celestine -l fi    |
+------------+-------------+--------------------+
| French     | français    | celestine -l fr    |
+------------+-------------+--------------------+
| Irish      | Gaeilge     | celestine -l ga    |
+------------+-------------+--------------------+
| Croatian   | hrvatski    | celestine -l hr    |
+------------+-------------+--------------------+
| Hungarian  | magyar      | celestine -l hu    |
+------------+-------------+--------------------+
| Italian    | italiano    | celestine -l it    |
+------------+-------------+--------------------+
| Lithuanian | lietuvių    | celestine -l lt    |
+------------+-------------+--------------------+
| Latvian    | latviešu    | celestine -l lv    |
+------------+-------------+--------------------+
| Maltese    | Malti       | celestine -l mt    |
+------------+-------------+--------------------+
| Dutch      | Nederlands  | celestine -l nl    |
+------------+-------------+--------------------+
| Polish     | polski      | celestine -l pl    |
+------------+-------------+--------------------+
| Portuguese | português   | celestine -l pt    |
+------------+-------------+--------------------+
| Romanian   | română      | celestine -l ro    |
+------------+-------------+--------------------+
| Slovak     | slovenčina  | celestine -l sk    |
+------------+-------------+--------------------+
| Slovenian  | slovenščina | celestine -l sl    |
+------------+-------------+--------------------+
| Swedish    | svenska     | celestine -l sv    |
+------------+-------------+--------------------+

+--------------------+------------+-------------+-----------------+
| ISO 3166-1 alpha-2 | Language   | Translation |  command        |
+====================+============+=============+=================+
| bg                 | Bulgarian  | български   | celestine -l en |
+--------------------+------------+-------------+-----------------+
| cs                 | Czech      | čeština     | celestine -l cs |
+--------------------+------------+-------------+-----------------+
| da                 | Danish     | dansk       | celestine -l da |
+--------------------+------------+-------------+-----------------+
| de                 | German     | Deutsch     | celestine -l de |
+--------------------+------------+-------------+-----------------+
| el                 | Greek      | ελληνικά    | celestine -l el |
+--------------------+------------+-------------+-----------------+
| en                 | English    | English     | celestine -l en |
+--------------------+------------+-------------+-----------------+
| es                 | Spanish    | español     | celestine -l es |
+--------------------+------------+-------------+-----------------+
| et                 | Estonian   | eesti       | celestine -l et |
+--------------------+------------+-------------+-----------------+
| fi                 | Finnish    | suomi       | celestine -l fi |
+--------------------+------------+-------------+-----------------+
| fr                 | French     | français    | celestine -l fr |
+--------------------+------------+-------------+-----------------+
| ga                 | Irish      | Gaeilge     | celestine -l ga |
+--------------------+------------+-------------+-----------------+
| hr                 | Croatian   | hrvatski    | celestine -l hr |
+--------------------+------------+-------------+-----------------+
| hu                 | Hungarian  | magyar      | celestine -l hu |
+--------------------+------------+-------------+-----------------+
| it                 | Italian    | italiano    | celestine -l it |
+--------------------+------------+-------------+-----------------+
| lt                 | Lithuanian | lietuvių    | celestine -l lt |
+--------------------+------------+-------------+-----------------+
| lv                 | Latvian    | latviešu    | celestine -l lv |
+--------------------+------------+-------------+-----------------+
| mt                 | Maltese    | Malti       | celestine -l mt |
+--------------------+------------+-------------+-----------------+
| nl                 | Dutch      | Nederlands  | celestine -l nl |
+--------------------+------------+-------------+-----------------+
| pl                 | Polish     | polski      | celestine -l pl |
+--------------------+------------+-------------+-----------------+
| pt                 | Portuguese | português   | celestine -l pt |
+--------------------+------------+-------------+-----------------+
| ro                 | Romanian   | română      | celestine -l ro |
+--------------------+------------+-------------+-----------------+
| sk                 | Slovak     | slovenčina  | celestine -l sk |
+--------------------+------------+-------------+-----------------+
| sl                 | Slovenian  | slovenščina | celestine -l sl |
+--------------------+------------+-------------+-----------------+
| sv                 | Swedish    | svenska     | celestine -l sv |
+--------------------+------------+-------------+-----------------+


Inspiration
***********
`Safebooru`_ - And the thousands of other booru sites.

`Board Game Geek`_ - Epic advancned search.

Info
****
`Semantic Versioning 2.0.0`_

`Write to me`_


.. _`Blender`: https://www.blender.org/
.. _`Board Game Geek`: https://boardgamegeek.com/advsearch/boardgame">
.. _`Celestine`: https://test.pypi.org/project/celestine/
.. _`Curses`: https://docs.python.org/3/howto/curses.html
.. _`Dear PyGui`: https://github.com/hoffstadt/DearPyGui/
.. _`More Itertools`: https://pypi.org/project/Pillow/
.. _`Pillow`: https://pypi.org/project/Pillow/
.. _`Pygame`: https://www.pygame.org/
.. _`Safebooru`: https://safebooru.org
.. _`Semantic Versioning 2.0.0`: https://semver.org/
.. _`Tkinter`: https://docs.python.org/3/library/tk.html
.. _`Windows Curses`: https://github.com/zephyrproject-rtos/windows-curses/
.. _`Write to me`: celestine@mem-dixy.ch
.. _PyPi: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-pypi
.. _python: https://www.python.org/downloads/
.. _unittest: https://docs.python.org/3/library/unittest.html
