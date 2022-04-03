[PIV-Tag](https://github.com/mem-dixy/PIV-Tag/) - (Personal, Portable, Private) Image Viewing Tag System
====================================================================================

- [About](#about)
- [Goals](#goals)
- [License](#license)
- [Requirements](#requirements)
- [Inspiration](#inspiration)
- [Installation](#installation)


About
--------------------------------------
View and organize your photos. Work in progress. Not currently functional.

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


License
--------------------------------------
EUROPEAN UNION PUBLIC LICENCE v. 1.2\
EUPL © the European Union 2007, 2016

Requirements
--------------------------------------
(Need to update this at some point. Try Instalation to get current code working.)

Recomended
Python `>= 3.4` (Lib/base64.py)\
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
[POV-Ray](https://www.povray.org/) - The Persistence of Vision Raytracer (Name look familar?)\
[Safebooru](https://safebooru.org/) - Safebooru (And the thousands of other booru sites.)\
[BGG](https://boardgamegeek.com/advsearch/boardgame) - Board Game Geek (Epic advancned search.)




Installation
--------------------------------------
| Package | [PyPi](https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing) |
| ------------------------------------------------------------------- | ----------------------- |
| [DearPyGui](https://github.com/hoffstadt/DearPyGui#installation) | `pip install dearpygui` |
| [Pillow](https://pillow.readthedocs.io/en/latest/installation.html) | `pip install Pillow` |

# Random notes






b binary:\
+ includes it\
- excludes it (NOT)\
\
WHERE pig AND dog\
WHERE NOT pig AND dog\
WHERE pig AND NOT dog\
WHERE NOT pig AND NOT dog\
WHERE pig OR dog\
WHERE NOT pig OR dog\
WHERE pig OR NOT dog\
WHERE NOT pig OR NOT dog\
\
\
\
s symbol:\
& puts it into AND group\
| puts it into OR group\
\
if set empty, use true\
WHERE TRUE AND TRUE\
WHERE (pig AND dog) AND TRUE\
WHERE TRUE AND (cat OR frog)\
WHERE (pig AND dog) AND (cat OR frog)\
\
& = ()&()\
| = ()|()\
\
\
(a & B) | (C | D)\
\
a b c d\
A & B & C & D\
a -b c -d\
A & !B & C & !D\
\
+a +b +c +d\
A & B & C & D\
+a -b +c -d\
A & !B & C & !D\
\
&&abc\
(a&(b&c))\
&&abc\
((a)&(b))&(c)\
&|abc\
((a)|(b))&(c)\
\
|&a|bcde\
abc|d&e|\
(((a & (b | c)) & d) | e)\
\

steps\
0 user input\
1 strip out all illegal characters. pass over each character and move to new buffer if valid\
2 convert invalid characters to valid character in new buffer\
3 remove all whitespace. separate items to token groups\
4 apply found symbols to new class. when hit tag, previously applied attributes are used. otherwise defaults used. state set each time new symbol seen, so in essence, last one seen used


filename:
sha3 512 base 16
sha3_512__18446744073709551616




requirements
