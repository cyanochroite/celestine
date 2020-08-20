from mem_dixy.tag.alphabet import convert
from mem_dixy.tag.alphabet import tag
from mem_dixy.tag.alphabet import hashy
from mem_dixy.tag.alphabet import space

from enum import Enum


class State(Enum):
    NONE = 1
    TAG = 2
    HASH = 3
    SPACE = 3


#string = input("you ugly")
string = "-🌋 Volcano🏕️ Camping🏜️ Desert"


falcon = []
falcon.append("[")

for character in string:
    falcon.append(convert.get(character, str()))

falcon.append("]")
bird = str().join(falcon)

tigger = []
token = []

state_now = State.NONE
state_past = State.NONE


def add_token():
    global tigger
    global token
    token.append(str().join(tigger))
    tigger = []


for character in bird:

    if character in tag:
        state_now = State.TAG

    elif character in hashy:
        state_now = State.HASH

    elif character in space:
        state_now = State.SPACE

    else:
        state_now = State.NONE

    if state_past is not state_now:
        add_token()

    tigger.append(character)
    state_past = state_now

print(string)
print(bird)
print(tigger)
print(token)
