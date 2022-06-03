from curses import wrapper
from curses import *

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    init_pair(1, COLOR_RED, COLOR_BLACK)
    init_pair(2, COLOR_GREEN, COLOR_BLACK)
    init_pair(3, COLOR_BLUE, COLOR_BLACK)

    stdscr.addstr("RANDOM QUOTES", A_REVERSE)
    stdscr.chgat(-1, A_REVERSE)

    stdscr.chgat(20, 7, 1, A_BOLD | color_pair(2))
    stdscr.chgat(20, 35, 1, A_BOLD | color_pair(1))
    
    quote_window = newwin(19, 80, 1, 0)
    quote_text_window = quote_window.subwin(14, 76, 3, 2)

    quote_text_window.addstr("Press 'R' to get your first quote!")
    quote_window.box()
    
    stdscr.noutrefresh()
    quote_window.noutrefresh()
    doupdate()


    while True:
        c = quote_window.getch()
        if c == ord('r') or c == ord('R'):
            quote_text_window.clear()
            quote_text_window.addstr("getting quote...", color_pair(3))
            quote_text_window.refresh()
            quote_text_window.clear()
            quote_text_window.addstr("NEW JOKE")
        elif c == ord('q') or c == ord('Q'):
            break

        stdscr.noutrefresh()
        quote_window.noutrefresh()
        quote_text_window.noutrefresh()
        doupdate()
        


    stdscr.refresh()
    stdscr.getkey()

wrapper(main)