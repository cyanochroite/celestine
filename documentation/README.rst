Celestine
#########

.. image:: https://readthedocs.org/projects/celestine/badge/?version=latest
   :target: https://celestine.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


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

Installation
************

Required
^^^^^^^^

Install from pip::

    pip install celestine

Optional
^^^^^^^^

If you want celestine to be more then just a command line tool, you will likely want one of these installed:
(Pygame has not yet been released for Python 3.11.) (Blender is hard so it has fallen behind in upkeep.)

+-------------------+----------------------+---------------------------------------+------------------------------------------------------------------------+
| Interface         | Type                 | How                                   | Information                                                            |
+===================+======================+=======================================+========================================================================+
| `Blender`_        | Application          | Install celestine as a Blender Add-on | Secondary scripts, called Add-ons, that extends Blender functionality. |
+-------------------+----------------------+---------------------------------------+------------------------------------------------------------------------+
| `Dear PyGui`_     | Python Package Index | pip install dearpygui                 | DearPyGui: A simple Python GUI Toolkit.                                |
+-------------------+----------------------+---------------------------------------+------------------------------------------------------------------------+
| `Pygame`_         | Python Package Index | pip install pygame                    | Python Game Development.                                               |
+-------------------+----------------------+---------------------------------------+------------------------------------------------------------------------+
| `Windows Curses`_ | Python Package Index | pip install windows-curses            | Support for the standard curses module on Windows.                     |
+-------------------+----------------------+---------------------------------------+------------------------------------------------------------------------+


The Python Programming Language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently supporting Python 3.11 (Used to support Python 3.10)

This is a Python application, and so it needs Python in order to run.
Don't feel like installing Python? Try running it in Blender insead!
(Blender support comming soon.)

Application
^^^^^^^^^^^

Some applications that come with it.

+-------------+-------------------------+------------------------------------------------------------------+
| Application | Command                 | Information                                                      |
+=============+=========================+==================================================================+
| Demo        | celestine -a demo       | Change screens with two whole buttons.                           |
+-------------+-------------------------+------------------------------------------------------------------+
| Translator  | celestine -a translator | Translate the default language file into the 24 other languages. |
+-------------+-------------------------+------------------------------------------------------------------+
| Viewer      | celestine -a viewer     | View a very small amount of pictures at once.                    |
+-------------+-------------------------+------------------------------------------------------------------+

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

Language
^^^^^^^^
The EU is characterised by its cultural and linguistic diversity, and the languages spoken in EU countries are an essential part of its cultural heritage. This is why the EU supports multilingualism in its programmes and in the work of its institutions.

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

Resources
*********

Learn more at `Read the Docs`_.

Join the `Discord`_.

`Email`_ the author.

.. _`Blender`: https://www.blender.org/
.. _`Celestine`: https://pypi.org/project/celestine/
.. _`Curses`: https://docs.python.org/3/howto/curses.html
.. _`Dear PyGui`: https://github.com/hoffstadt/DearPyGui/
.. _`Discord`: https://discord.gg/aNmDWPXd7B
.. _`Email`: celestine@mem-dixy.ch
.. _`Pygame`: https://www.pygame.org/
.. _`Read the Docs`: https://celestine.readthedocs.io/en/latest/
.. _`Tkinter`: https://docs.python.org/3/library/tk.html
.. _`Windows Curses`: https://github.com/zephyrproject-rtos/windows-curses/
