The Celestine Image Viewer
====================================================================================

- [About](#about)
- [Goals](#goals)
- [Requirements](#requirements)
- [Inspiration](#inspiration)
- [Installation](#installation)


About
--------------------------------------
View, tag, and organize your photos. Work in progress. Not currently functional.

Old Description:
By default this is a command line application. Should work anywhere Python 3 code can be run. The code has several folders dedicated to specific pluggins. If package not found, code not run. Can actually be deleted if desired.

Older description:
Decided that the main reason behind this was an attempt to use HTML as my GUI.
Most files in this project are dedicated to viewing and modifying local images.
Will try to update the project to reflect that.


Goals
--------------------------------------
- Zero internet access. (An offline only application. Possible exception would be checking for updates.)
- Minimal dependencies. (Ideally no more than 4 pip installs. Currently at 2.)
- Advanced tag searching. (Most websites have really lousy topic filters.)

What this is not:
- This is not a photo editor.
- This is not a photo downloader.
- This is not a mobile application.


Requirements
--------------------------------------
(Need to update this at some point. Try Instalation to get current code working.)

Recomended
Python `>= 3.9` (PEP 584)\
Pillow `>= 7.2.0` (TIFF BYTE tags format)\

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
--------------------------------------
[Safebooru](https://safebooru.org/) - And the thousands of other booru sites.\
[Board Game Geek](https://boardgamegeek.com/advsearch/boardgame) - Epic advancned search.


Installation
--------------------------------------
| Package | [PyPi](https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing) |
| ------------------------------------------------------------------- | ----------------------- |
| [DearPyGui](https://github.com/hoffstadt/DearPyGui#installation) | `pip install dearpygui` |
| [Pillow](https://pillow.readthedocs.io/en/latest/installation.html) | `pip install Pillow` |
