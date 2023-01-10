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


Primary
Secondary
Tertiary
Quaternary
Quinary
secondary, tertiary, and quaternary layers


I believe that record is held by the codepoint U+FBF9 (ﯹ), “ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH HAMZA ABOVE WITH ALEF MAKSURA ISOLATED FORM,” which is 83 characters. There are a couple of other Arabic ligatures that are close to that count, as well.
The next longest name for a different sort of character is U+1F502 (🔂), “CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS WITH CIRCLED ONE OVERLAY” which is 78 characters.





Add a "py.typed" file
https://devblogs.microsoft.com/python/pylance-introduces-five-new-features-that-enable-type-magic-for-python-developers/






LATIN CAPITAL LETTER A WITH RING ABOVE = 212B
LATIN CAPITAL LETTER ETH = 0
LATIN CAPITAL LETTER O WITH STROKE
LATIN SMALL LETTER SHARP S
LATIN SMALL LETTER AE






# Random notes


Rexex parser: Adds support for wildcard searches using '*'.


command core
only the basics here
use on web server or as external library




b binary:
+ includes it
- excludes it (NOT)

WHERE pig AND dog
WHERE NOT pig AND dog
WHERE pig AND NOT dog
WHERE NOT pig AND NOT dog
WHERE pig OR dog
WHERE NOT pig OR dog
WHERE pig OR NOT dog
WHERE NOT pig OR NOT dog



s symbol:
& puts it into AND group
| puts it into OR group

if set empty, use true
WHERE TRUE AND TRUE
WHERE (pig AND dog) AND TRUE
WHERE TRUE AND (cat OR frog)
WHERE (pig AND dog) AND (cat OR frog)

& = ()&()
| = ()|()


(a & B) | (C | D)

a b c d
A & B & C & D
a -b c -d
A & !B & C & !D

+a +b +c +d
A & B & C & D
+a -b +c -d
A & !B & C & !D


does white space matter?
no

steps
0 user input
1 strip out all illegal characters. pass over each character and move to new buffer if valid
2 convert invalid characters to valid character in new buffer
3 remove all whitespace. separate items to token groups
4 apply found symbols to new class. when hit tag, previously applied attributes are used. otherwise defaults used. state set each time new symbol seen, so in essence, last one seen used



filename:
sha3 512 base 16
sha3_512__18446744073709551616





development install
unittest
pytest

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

https://semver.org/

https://libraries.io/

celestine.readthedocs.io
celestine.rtfd.io




PACKAGE
python -m pip install --upgrade pip
python -m pip install --upgrade build
python -m pip install --upgrade twine
python -m build
python -m twine check --strict dist/*


# test
python -m twine upload --verbose --repository testpypi dist/*
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps celestine
python -m pip install --index-url https://test.pypi.org/simple/ celestine


# real
python -m twine upload --verbose dist/*
python -m pip install celestine

INSTALL
pip install pytest
pip install coverage



SHELL COMMAND
# quick test
python -m pytest

# test code used
python -m coverage run --source=celestine/application/unittest --module pytest --verbose

python -m coverage run --source=tests --module pytest --verbose
python -m coverage report --show-missing
python -m coverage html

# source code used by test code
python -m coverage run --module pytest --verbose celestine/application/unittest
python -m coverage report --show-missing
python -m coverage html

# source code used
python -m coverage run --source=celestine --module pytest --verbose celestine/application/unittest
python -m coverage report --show-missing
python -m coverage html




pip install more-itertools
pip install pylint

requests
uuid

AZURE API for translationts




python -m pip install --requirement requirements.txt

python -m pip install windows-curses

UniCurses 1.2 ??


https://packaging.python.org/en/latest/tutorials/installing-packages/#requirements-for-installing-packages


GUI to try:
pip install wxPython
pip install pygame
pip install Kivy


PACKAGE
where packages that change functionality, mostly guis
no fallback support. either it works or not
typically only one of these would be run ever, and only 1 at once


EXTENSION
is where extra packages can be installed for more functionality
will try to provide fallback options so every feature "works"
idea is all of them would be installed usually


ToDo Features:
Add gamma to photos? Both TK and dearpygui support this


A	true	++
B	anti	-+
C	both	--
D	zero	+-

+-----+------+------+------+------+
| AND | same | not  | inv  | flip |
+=====+======+======+======+======+
| A   | A    | B    | C    | D    |
+-----+------+------+------+------+
| B   | B    | A    | D    | C    |
+-----+------+------+------+------+
| C   | C    | D    | A    | B    |
+-----+------+------+------+------+
| D   | D    | C    | B    | A    |
+-----+------+------+------+------+


+-----+---+---+---+---+
| AND | A | B | C | D |
+=====+===+===+===+===+
| A   | A | B | C | D |
+-----+---+---+---+---+
| B   | B | B | C | D |
+-----+---+---+---+---+
| C   | C | C | C | D |
+-----+---+---+---+---+
| D   | D | D | D | D |
+-----+---+---+---+---+

+-----+---+---+---+---+
| OR  | A | B | C | D |
+=====+===+===+===+===+
| A   | A | A | A | A |
+-----+---+---+---+---+
| B   | A | B | B | B |
+-----+---+---+---+---+
| C   | A | B | C | C |
+-----+---+---+---+---+
| D   | A | B | C | D |
+-----+---+---+---+---+
