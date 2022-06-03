import curses

def draw_menu(stdscr):
    k = 0
    kw = 0
    kk = ""
    height, width = stdscr.getmaxyx()
    min_x_keystr = width - 1
    min_x_wkeystr = width - 1
    min_x_kkeystr = width - 1
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        #stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "Curses example"[:width-1]
        subtitle = "Written by Clay McLeod"[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]
        else:
            keystr = "Last key pressed: {}".format(k)[:width-1]
        if kw == 0:
            wkeystr = "No wide key press detected..."[:width-1]
        else:
            wkeystr = "Last wide key pressed: {}".format(kw)[:width-1]
        if kk == 0:
            kkeystr = "No 'key' press detected..."[:width-1]
        else:
            kkeystr = "Last 'key' pressed: {}".format(kk)[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_x_wkeystr = int((width // 2) - (len(wkeystr) // 2) - len(wkeystr) % 2)
        start_x_kkeystr = int((width // 2) - (len(kkeystr) // 2) - len(kkeystr) % 2)
        start_y = int((height // 2) - 2)
        min_x_keystr = min(min_x_keystr, start_x_keystr)
        min_x_wkeystr = min(min_x_wkeystr, start_x_wkeystr)
        min_x_kkeystr = min(min_x_kkeystr, start_x_kkeystr)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        stdscr.addstr(start_y + 7, start_x_wkeystr, wkeystr)
        stdscr.addstr(start_y + 9, start_x_kkeystr, kkeystr)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

        # Get wide-char version
        curses.ungetch(k)
        kw = stdscr.get_wch()

        # Get key version
        if isinstance(kw, str):
            curses.unget_wch(kw)
        else:
            curses.ungetch(kw)
        kk = stdscr.getkey()

        # Clear the keystroke text
        stdscr.move(start_y + 5, min_x_keystr)
        stdscr.clrtoeol()
        stdscr.move(start_y + 7, min_x_wkeystr)
        stdscr.clrtoeol()
        stdscr.move(start_y + 9, min_x_kkeystr)
        stdscr.clrtoeol()
        stdscr.refresh()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
    

import dearpygui.dearpygui as dpg

VERSION = 1


class Window():
    end = [
        "stop",
        "die",
        "end",
        "kill",
        "done"
    ]

    def draw(self):
        with dpg.window(tag="primary_window"):
            dpg.add_text("Hello, world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string", default_value="Quick brown fox")
            dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    def run(self):
        pass
