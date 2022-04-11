import sys
sys.path.insert(1, '../src/')

# from tag.alphabet import convert
# from tag.alphabet import tag
# from tag.alphabet import hashy
# from tag.alphabet import space
#from tag.alphabet import *



from tag.alphabet import convert
from tag.alphabet import letter
from tag.alphabet import comparison
from tag.alphabet import all_token
from tag.alphabet import one_token
from unicode.u0000 import LOW_LINE


from enum import Enum


class State(Enum):
    NONE = 1
    TAG = 2
    HASH = 3
    SPACE = 3
    SYMBOL = 4


# string = input("you ugly")
string = open("input.txt", encoding="utf_8").readline()


falcon = []

for character in string:
    falcon.append(convert.get(character, str()))

bird = str().join(falcon)

tigger = []
mouse = []

state_now = State.NONE
state_past = State.NONE





def add_token():
    global tigger
    global mouse
    value = str().join(tigger)
    hold = []
    start = False
    end = False
    for character in value:
        start = character is not LOW_LINE
        end |= start
        if end:
            hold.append(character)

    value = str().join(hold)
    cat = Atag(value)

    mouse.append(cat)
    tigger = []


def parse(string):
    is_letter = False
    was_letter = False
    is_comparison = False
    was_comparison = False
    for character in bird:
        was_letter = is_letter
        is_letter = character in letter
        if was_letter and not is_letter:
            add_token()

        was_comparison = is_comparison
        is_comparison = character in comparison
        if was_comparison and not is_comparison:
            add_token()

        if character in all_token:
            tigger.append(character)

        if character in one_token:
            add_token()

    add_token()

    print(string)
    print(bird)
    print(tigger)
    print(mouse)


print("START")
print(string)


class translator():
    @staticmethod
    def translate(string):
        return str().join(
            [
                item for item in
                [convert.get(character) for character in string]
                if item is not None
            ]
        )

class tokenizer():
    @staticmethod
    def tokenize(string):
        return string

class parser():
    @staticmethod
    def parse(string):
        return string.split()

string = translator.translate(string)
string = tokenizer.tokenize(string)
string = parser.parse(string)

print("OLD")
parse(string)
