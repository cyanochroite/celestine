The Celestine Image Viewer
##########################

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    note
    wing

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

Development settings at :doc:`wing`.
Project notes at :doc:`note`.


.. _Goals:

Primary Goals
*************
- Is an offline only application. (The only internet used is when you use pip.)
- Minimal required dependencies. (All you need to run this package is Python.)
- Can be customized to use different packages. (See the list below for supported packages.)
- Free. No cost for use, distributions, plugins, maintenece, support.


Offline Only
^^^^^^^^^^^^
The only internet you need is when you install with pip.



Privacy and Internet access
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Celestine respects your privacy, no registration is needed, no connection to the internet is made if you decide to install and use Celestine. Celestine does not need internet to function properly.

Some add-ons bundled with Celestine may access the internet for additional services. These add-ons are not enabled on installing Celestine. These add-ons are not required to be enabled for proper functioning of the software, nor will any Celestine function ask for enabling such add-ons.

Add-ons that require internet will ask a user explicit permission to use internet while or after enabling the add-on.

Note: this applies to the official version provided via GitHub. We always recommend you to use the official releases.



Your Artwork
^^^^^^^^^^^^
What you create with Celestine is your sole property. All your artwork – images or movie files – including the .blend files and other data files Celestine can write, is free for you to use as you like.

That means that Celestine can be used commercially by artists, by studios to make animation films or VFX, by game artists to work on commercial games, by scientists for research, and by students in educational institutions.

Celestine's license guarantees you this freedom. Nobody is ever permitted to take it away, in contrast to trial or “educational” versions of commercial software that will forbid your work in commercial situations.


No Required Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

The goal is that this will run without any external dependencies.
Which means you can just download the source code and it will just work.
However, this uses a Graphical User Interface, and Python does not (always) come with a Graphical User Interface.
In this case, it will run, but it will not do much or be very easy to use. This is a problem.

The solution is to make it appear as if this runs without any external dependencies.
There are a lot of Graphical User Interfaces out there, and odds are the user has at least one of them installed.
So, all I need to do is to support all the major ones and I can achieve the goal.


Free
^^^^^^^^^^^^^^^^^^^^^^^^

Free from ads, promotions, sales, spyware, keyloggers, prorietary content.
No begging for likes, subscribes, popularity, donations, patrions.

I will never ask for money for this project. So if you see someone claiming you need to pay money, it is a scam.



I very much like the model Blender uses. So I just copy and pasted what they said here and will adjust the wording later.



The Software

Blender is released under the GNU General Public License (GPL, or “free software”).

This license grants people a number of freedoms:

    You are free to use Blender, for any purpose
    You are free to distribute Blender
    You can study how Blender works and change it
    You can distribute changed versions of Blender

The GPL strictly aims at protecting these freedoms, requiring everyone to share their modifications when they also share the software in public. That aspect is commonly referred to as Copyleft.

The Blender Foundation and its projects on blender.org are committed to preserving Blender as free software.
License details

The source code we develop at blender.org is default being licensed as GNU GPL Version 2 or later. Some modules we make are using more permissive licenses, though, for example, the Blender Cycles rendering engine is available as Apache 2.0.

Blender also uses many modules or libraries from other projects. For example, Python uses the Python License; Bullet uses the Zlib License; Libmv uses the MIT License; and OSL, a BSD License.

All the components that together make Blender are compatible under the newer GNU GPL Version 3. That is also the license to use for any distribution of Blender binaries.
Your Artwork

What you create with Blender is your sole property. All your artwork – images or movie files – including the .blend files and other data files Blender can write, is free for you to use as you like.

That means that Blender can be used commercially by artists, by studios to make animation films or VFX, by game artists to work on commercial games, by scientists for research, and by students in educational institutions.

Blender’s GNU GPL license guarantees you this freedom. Nobody is ever permitted to take it away, in contrast to trial or “educational” versions of commercial software that will forbid your work in commercial situations.
Privacy and Internet access

Blender respects your privacy, no registration is needed, no connection to the internet is made if you decide to install and use Blender. Blender does not need internet to function properly.

Some add-ons bundled with Blender may access the internet for additional services. These add-ons are not enabled on installing Blender. These add-ons are not required to be enabled for proper functioning of the software, nor will any Blender function ask for enabling such add-ons.

Add-ons that require internet will ask a user explicit permission to use internet while or after enabling the add-on.

Note: this applies to the official version provided via blender.org. We always recommend you to use the official releases.

Sharing or selling Blender add-ons (Python scripts)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Blender’s Python API is an integral part of the software, used to define the user interface or develop tools for example. The GNU GPL license therefore requires that such scripts (if published) are being shared under a GPL compatible license. DO NOT SELL SUCH SCRIPTS. Your customers will receive the script under the same license (GPL), with the same free conditions as everyone has for Blender.









All addons and plugins, skins, textures, whatever, should also be free.

No:
DLC, micro transactions, premium, patron, special stuff, ads,
clickbait, promotions, donations, NFTs.

Way to many people and games do this and its super annoying.
This is free for everyone, hopefully forever. Lets keep it that way.


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
