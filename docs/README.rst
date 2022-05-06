Section Title 1
###############

Section Title 2
***************

Section Title 3
^^^^^^^^^^^^^^^

Section Title 4
~~~~~~~~~~~~~~~

Section Title 5
"""""""""""""""

Section Title 6
'''''''''''''''

The Celestine Image Viewer
##########################

- About_
- `Primary Goals`_
- Requirements_
- Inspiration_
- Info_

candy


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


Primary Goals
*************
- Is an offline only application. (The only internet used is when you use pip.)
- Has no required dependencies. (All you need to run this package is Python.)
- Can be customized to use different packages. (See the list below for supported packages.)


Offline Only
^^^^^^^^^^^^
The only internet you need is when you install with pip.

No Dependencies
^^^^^^^^^^^^^^^
Just download and run.

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
+-----------+----------+-------------------+----------------------------------------+
| Python    | Need     | Optional Features | Why                                    |
+===========+==========+===================+========================================+
| Python_   | REQUIRED |                   | This project is written in Python.     |
+-----------+----------+-------------------+----------------------------------------+
| tkinter_  | OPTIONAL | tcl/tk and IDLE   | Use this if you don't trust DearPyGui. |
+-----------+----------+-------------------+----------------------------------------+
| unittest_ | OPTIONAL | Python test suite | Use this to run the tests yourself.    |
+-----------+----------+-------------------+----------------------------------------+

.. _Python: https://www.python.org/downloads/
.. _tkinter: https://docs.python.org/3/library/tkinter.html
.. _unittest: https://docs.python.org/3/library/unittest.html

+---------------------------+-------------+-----------------------+-----------------------------------------------------+
| Package                   | Need        | PyPi_                 | Why                                                 |
+===========================+=============+=======================+=====================================================+
| `Celestine Image Viewer`_ | REQUIRED    |                       | This is the project you are trying to install.      |
+---------------------------+-------------+-----------------------+-----------------------------------------------------+
| DearPyGui_                | RECOMMENDED | pip install dearpygui | Without this, you need tkinter or the command line. |
+---------------------------+-------------+-----------------------+-----------------------------------------------------+
| Pillow_                   | RECOMMENDED | pip install Pillow    | Without this most images wont load.                 |
+---------------------------+-------------+-----------------------+-----------------------------------------------------+

.. _PyPi: https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-pypi
.. _`Celestine Image Viewer`: https://github.com/mem-dixy/celestine-viewer/
.. _DearPyGui: https://pypi.org/project/dearpygui/
.. _Pillow: https://pypi.org/project/Pillow/

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
.. _`Write to me`: celestine-viewer@mem-dixy.ch