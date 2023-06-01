import curses
import math

def main(stdscr):
    #curses.start_color()
    #curses.use_default_colors()

    print(curses.COLORS)
    print(curses.COLOR_PAIRS)


    reserved = 8

    limit = min(curses.COLORS, curses.COLOR_PAIRS)
    # 8 reserved colors. Remaining split over 3 channels.
    split = (limit - reserved) ** (1/3)
    base = math.floor(split)

    power_zero = base ** 0
    power_one = base ** 1
    power_two = base ** 2
    power_three = base ** 3

    scale = 1000 // (base - 1)

    for index in range(reserved, reserved + power_three):
        color = index - reserved

        red = ((color // power_zero) % base) * scale
        green = ((color // power_one) % base) * scale
        blue = ((color // power_two) % base) * scale

        curses.init_color(index, red, green, blue)
        curses.init_pair(index, 0, index)







    for index in range(0, curses.COLOR_PAIRS):
        stdscr.addstr(str(index), curses.color_pair(index))

    stdscr.getch()


curses.wrapper(main)
