# image program
View and organize your photos.


# future
Decided that the main reason behind this was an attempt to use HTML as my GUI.
Most files in this project are dedicated to viewing and modifying local images.
Will try to update the project to reflect that.


# (Merge in old Read Me)

By default this is a command line application. Should work anywhere Python 3 code can be run. The code has several folders dedicated to specific pluggins. If package not found, code not run. Can actually be deleted if desired.



Requirements:
Python


Recomended
Python 3.4 (Lib/base64.py)
Python 3.9 (PEP 584)

Pillow 7.2.0 (TIFF BYTE tags format)
Replaced TiffImagePlugin DEBUG with logging
Corrected default offset when writing EXIF data
Moved to ImageFileDirectory_v2 in Image.Exif
TIFF BYTE tags format



Recommended Packages:
Tkinter: Included in most python distributions, which means no installation or setup required. Adds GUI to application. Makes it easier for the average user to use. (Plus now you can actually see the images.)

Pillow: InstaLibrary for loading images. Allows for many image file types.


Optional Packages:
-None-
Additional GUI libraries and features may be added in the future. Some configuration may be needed to toggle these additional features.

Rexex parser: Adds support for wildcard searches using '*'.


command core
only the basics here
use on web server or as external library




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
