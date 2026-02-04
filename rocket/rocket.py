import curses
from time import sleep
from math import floor

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    center = floor(curses.COLS / 2)
    ground = curses.LINES - 1
    flames = ground
    while flames >= 0:
        if flames < ground:
            stdscr.addstr(flames + 1, center - 5, '          ')
        if flames > 0:
            stdscr.addstr(flames, center - 2, '/ | \\')
        if flames > 1:
            stdscr.addstr(flames - 1, center - 2, '|___|')
        if flames > 2:
            stdscr.addstr(flames - 2, center - 2, '|   |')
        if flames > 3:
            stdscr.addstr(flames - 3, center - 2, '| A |')
        if flames > 4:
            stdscr.addstr(flames - 4, center - 2, '| S |')
        if flames > 5:
            stdscr.addstr(flames - 5, center - 2, '| U |')
        if flames > 6:
            stdscr.addstr(flames - 6, center - 2, '|   |')
        if flames > 7:
            stdscr.addstr(flames - 7, center - 2, ' / \\ ')
        if flames > 8:
            stdscr.addstr(flames - 8, center - 2, '  ^  ')
        stdscr.refresh()
        flames = flames - 1
        tts = floor(flames / 10)
        if tts < 1:
            tts = 1
        sleep(tts)
    stdscr.addstr(ground, 0, "Press any key...")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
