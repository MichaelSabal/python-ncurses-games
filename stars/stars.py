import curses
from random import randint
from time import sleep
from math import floor

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK)

    stdscr.nodelay(True)
    stdscr.immedok(True)
    stdscr.clear()
    curses.curs_set(0)
    totalDots = curses.LINES * curses.COLS
    percentFill = randint(1, 50)
    maxDots = floor(totalDots * (percentFill / 100))
    dotsList = []
    while stdscr.getch() == -1:
        atLine = randint(0, curses.LINES - 1)
        atCol = randint(0, curses.COLS - 1)
        if len(dotsList) >= maxDots and not [atLine, atCol] in dotsList:
            continue
        baseColor = curses.color_pair(randint(1, 8))
        brightFlag = randint(0, 1)
        if brightFlag == 1:
            textColor = baseColor | curses.A_BOLD
        else:
            textColor = baseColor | curses.A_NORMAL
        stdscr.addstr(atLine, atCol, '*', textColor)
        dotsList.append([atLine, atCol])
        sleep(1)

curses.wrapper(main)

