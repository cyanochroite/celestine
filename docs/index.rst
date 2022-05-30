The Celestine Image Viewer
##########################

- About_
- Goals_
- Requirements_
- Inspiration_
- Info_

.. image:: https://readthedocs.org/projects/celestine/badge/?version=latest
   :target: https://celestine.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

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

.. _Goals:

Primary Goals
*************
- Is an offline only application. (The only internet used is when you use pip.)
- Has no required dependencies. (All you need to run this package is Python.)
- Can be customized to use different packages. (See the list below for supported packages.)


Offline Only
^^^^^^^^^^^^
The only internet you need is when you install with pip.

No Required Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^
Celestine is very independent and can run without any dependecies.
However she also likes gifts. Try giving her a Package_.

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

.. _Requirements:

Requirements
************
+-----------+----------+-------------------+----------------------------------------+
| Python    | Need     | Optional Features | Why                                    |
+-----------+----------+-------------------+----------------------------------------+
| Python_   | REQUIRED |                   | This project is written in Python.     |
+-----------+----------+-------------------+----------------------------------------+
| tkinter_  | OPTIONAL | tcl/tk and IDLE   | Use this if you don't trust DearPyGui. |
+-----------+----------+-------------------+----------------------------------------+
| unittest_ | OPTIONAL | Python test suite | Use this to run the tests yourself.    |
+-----------+----------+-------------------+----------------------------------------+

.. _Python: https://www.python.org/downloads/
.. _tkinter: https://docs.python.org/3/library/tkinter.html
.. _unittest: https://docs.python.org/3/library/unittest.html

Package
********

These packages are optional. But features and performance may be lacking without them.

+-------------------+----------------------------+------------------------------------------------------------+
| Package           | Install                    | Description                                                |
+===================+============================+============================================================+
| `Dear PyGui`_     | pip install dearpygui      | DearPyGui: A simple Python GUI Toolkit                     |
+-------------------+----------------------------+------------------------------------------------------------+
| `More Itertools`_ | pip install more-itertools | More routines for operating on iterables, beyond itertools |
+-------------------+----------------------------+------------------------------------------------------------+
| `Pillow`_         | pip install Pillow         | Python Imaging Library (Fork)                              |
+-------------------+----------------------------+------------------------------------------------------------+


.. _PyPi: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-pypi
.. _`Celestine`: https://test.pypi.org/project/celestine/
.. _`Dear PyGui`: https://pypi.org/project/dearpygui/
.. _`Pillow`: https://pypi.org/project/Pillow/
.. _`More Itertools`: https://pypi.org/project/Pillow/

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

.. _Inspiration:

Inspiration
***********
`Safebooru`_ - And the thousands of other booru sites.

`Board Game Geek`_ - Epic advancned search.

.. _`Safebooru`: https://safebooru.org
.. _`Board Game Geek`: https://boardgamegeek.com/advsearch/boardgame">

.. _Info:

Info
****
`Semantic Versioning 2.0.0`_

`Write to me`_

.. _`Semantic Versioning 2.0.0`: https://semver.org/
.. _`Write to me`: celestine@mem-dixy.ch