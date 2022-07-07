import curses


def draw_menu(stdscr):
    stdscr.clear()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.addstr("RANDOM QUOTES", curses.A_REVERSE)
    stdscr.chgat(-1, curses.A_REVERSE)

    stdscr.chgat(20, 7, 1, curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(20, 35, 1, curses.A_BOLD | curses.color_pair(1))

    quote_window = curses.newwin(19, 80, 1, 0)
    quote_text_window = quote_window.subwin(14, 76, 3, 2)

    quote_text_window.addstr("Press 'R' to get your first quote!")
    quote_window.box()

    stdscr.noutrefresh()
    quote_window.noutrefresh()
    curses.doupdate()

    while True:
        c = quote_window.getch()
        if c == ord('r') or c == ord('R'):
            quote_text_window.clear()
            quote_text_window.addstr("getting quote...", curses.color_pair(3))
            quote_text_window.refresh()
            quote_text_window.clear()
            quote_text_window.addstr("NEW JOKE")
        elif c == ord('q') or c == ord('Q'):
            break

        stdscr.noutrefresh()
        quote_window.noutrefresh()
        quote_text_window.noutrefresh()
        curses.doupdate()

    stdscr.clear()
    stdscr.refresh()

    k = 0
    kw = 0
    kk = ""
    height, width = stdscr.getmaxyx()
    min_x_keystr = width - 1
    min_x_wkeystr = width - 1
    min_x_kkeystr = width - 1

    cursor_x = 0
    cursor_y = 0

    # Loop where k is the last character pressed
    while (k != ord('q')):
        key = k
        if key == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif key == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif key == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif key == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        height, width = stdscr.getmaxyx()

        cursor_x = max(0, cursor_x)
        cursor_x = min(width - 1, cursor_x)
        cursor_y = max(0, cursor_y)
        cursor_y = min(height - 1, cursor_y)

        # Initialization
        # stdscr.clear()

        # Declaration of strings
        title = "Curses example"[:width - 1]
        subtitle = "Written by Clay McLeod"[:width - 1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width - 1]
        else:
            keystr = "Last key pressed: {}".format(k)[:width - 1]
        if kw == 0:
            wkeystr = "No wide key press detected..."[:width - 1]
        else:
            wkeystr = "Last wide key pressed: {}".format(kw)[:width - 1]
        if kk == 0:
            kkeystr = "No 'key' press detected..."[:width - 1]
        else:
            kkeystr = "Last 'key' pressed: {}".format(kk)[:width - 1]

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
        stdscr.addstr(height - 1, 0, statusbarstr)
        stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
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


curses.wrapper(draw_menu)
