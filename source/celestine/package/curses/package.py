"""
Pylint can't seem to find dearpygui and so gives a few errors.
Putting alias here to contain errors to this file only.
"""
# https://dearpygui.readthedocs.io/en/latest/
import curses
import _curses


def window(column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return curses.newwin(nlines, ncols, begin_y, begin_x)


def subwindow(window, column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return window.subwin(nlines, ncols, begin_y, begin_x)


def doupdate():
    curses.doupdate()


KEY_UP = curses.KEY_UP
KEY_DOWN = curses.KEY_DOWN
KEY_LEFT = curses.KEY_LEFT
KEY_RIGHT = curses.KEY_RIGHT
KEY_Q = 113  # ord('q'):
KEY_SPACE = 32  # ord(' ')

space = 32
quit = 113
down = 258
up = 259
left = 260
right = 261

noecho = _curses.noecho
initscr = _curses.initscr
cbreak = _curses.cbreak
start_color = _curses.start_color

echo = _curses.echo
nocbreak = _curses.nocbreak
endwin = _curses.endwin
