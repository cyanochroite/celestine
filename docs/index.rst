The Celestine Image Viewer
##########################

- About_
- Goals_
- Requirements_
- Inspiration_
- Info_

.. _About:

About
*****
View, tag, and organize your photos. Work in progress. Not currently functional.


By default this is a command line application.
Should work anywhere Python 3 code can be run.
The code has several folders dedicated to specific pluggins.
If package not found, code not run. Can actually be deleted if desired.

Older description:
Decided that the main reason behind this was an attempt to use HTML as my GUI.
Most files in this project are dedicated to viewing and modifying local images.
Will try to update the project to reflect that.

More
----

 * :doc:`wing`
 * :doc:`../extra/video-tutorials`


.. _Goals:

Primary Goals
*************
- Is an offline only application. (The only internet used is when you use pip.)
- Minimal required dependencies. (All you need to run this package is Python.)
- Can be customized to use different packages. (See the list below for supported packages.)


Offline Only
^^^^^^^^^^^^
The only internet you need is when you install with pip.

No Required Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

The goal is that this will run without any external dependencies.
Which means you can just download the source code and it will just work.
However, this uses a Graphical User Interface, and Python does not (always) come with a Graphical User Interface.
In this case, it will run, but it will not do much or be very easy to use. This is a problem.

The solution is to make it appear as if this runs without any external dependencies.
There are a lot of Graphical User Interfaces out there, and odds are the user has at least one of them installed.
So, all I need to do is to support all the major ones and I can achieve the goal.


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

Currently supporting Python 3.10 - 3.11

This is a Python application, and so it needs Python in order to run.
Don't feel like installing Python? Try running it in Blender insead!


A Graphical User Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want celestine to be more then just a command line tool, you will need at least one of these installed:

+-------------------+-------------------------+--------------------------------------------------------+-----------------------------------------------------------------------+
| Interface         | Type                    | How                                                    | Information                                                           |
+===================+=========================+========================================================+=======================================================================+
| `Blender`_        | Application             | Install celestine as a Blender Add-on                  | Secondary scripts, called Add-ons that extends Blender functionality. |
+-------------------+-------------------------+--------------------------------------------------------+-----------------------------------------------------------------------+
| `Curses`_         | Python Standard Library | Python Installer                                       | The Windows version of Python does not include the curses module.     |
+-------------------+-------------------------+--------------------------------------------------------+-----------------------------------------------------------------------+
| `Dear PyGui`_     | Python Package Index    | pip install dearpygui                                  | DearPyGui: A simple Python GUI Toolkit.                               |
+-------------------+-------------------------+--------------------------------------------------------+-----------------------------------------------------------------------+
| `Pygame`_         | Python Package Index    | pip install pygame                                     | Python Game Development.                                              |
+-------------------+-------------------------+--------------------------------------------------------+-----------------------------------------------------------------------+
| `Tkinter`_        | Python Standard Library | Python Installer > Optional Features > tcl/tk and IDLE | The tkinter package is a thin object-oriented layer on top of Tcl/Tk. |
+-------------------+-------------------------+--------------------------------------------------------+-----------------------------------------------------------------------+
| `Windows Curses`_ | Python Package Index    | pip install windows-curses                             | Support for the standard curses module on Windows.                    |
+-------------------+-------------------------+--------------------------------------------------------+-----------------------------------------------------------------------+

.. _`Blender`: https://www.blender.org/
.. _`Curses`: https://docs.python.org/3/howto/curses.html
.. _`Dear PyGui`: https://github.com/hoffstadt/DearPyGui/
.. _`Pygame`: https://www.pygame.org/
.. _`Tkinter`: https://docs.python.org/3/library/tk.html
.. _`Windows Curses`: https://github.com/zephyrproject-rtos/windows-curses/

Extensions
^^^^^^^^^^

These packages are optional. But features and performance may be lacking without them.

+-------------------+----------------------+----------------------------+-------------------------------------------------------------+
| Package           | Type                 | How                        | Information                                                 |
+===================+======================+============================+=============================================================+
| `More Itertools`_ | Python Package Index | pip install more-itertools | More routines for operating on iterables, beyond itertools. |
+-------------------+----------------------+----------------------------+-------------------------------------------------------------+
| `Pillow`_         | Python Package Index | pip install Pillow         | Python Imaging Library (Fork).                              |
+-------------------+----------------------+----------------------------+-------------------------------------------------------------+

.. _`More Itertools`: https://pypi.org/project/Pillow/
.. _`Pillow`: https://pypi.org/project/Pillow/




.. _python: https://www.python.org/downloads/
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _PyPi: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-pypi
.. _`Celestine`: https://test.pypi.org/project/celestine/





.. _python: https://www.python.org/downloads/
.. _unittest: https://docs.python.org/3/library/unittest.html

(Old notes. Still useful. Need to add to table above somehow.)

Recomended
Python `>= 3.9` (PEP 584)
Pillow `>= 7.2.0` (TIFF BYTE tags format)

Recommended Packages:
Tkinter: Included in most python distributions, which means no installation or setup required. Adds GUI to application. Makes it easier for the average user to use. (Plus now you can actually see the images.)

Pillow: InstaLibrary for loading images. Allows for many image file types.

Optional Packages:
Additional GUI libraries and features may be added in the future. Some configuration may be needed to toggle these additional features.

Rexex parser: Adds support for wildcard searches using '*'.


command core
only the basics here
use on web server or as external library

Inspiration
***********
`Safebooru`_ - And the thousands of other booru sites.

`Board Game Geek`_ - Epic advancned search.

.. _`Safebooru`: https://safebooru.org
.. _`Board Game Geek`: https://boardgamegeek.com/advsearch/boardgame">

Info
****
`Semantic Versioning 2.0.0`_

`Write to me`_

.. _`Semantic Versioning 2.0.0`: https://semver.org/
.. _`Write to me`: celestine@mem-dixy.ch
