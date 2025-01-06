import curses
from random import randint
from random import seed
from time import sleep, time
from math import floor

WORDLIST_SIZE = 51795

def drawFigure(stdscr, missesRemaining):
	if missesRemaining == 11:
		stdscr.addstr(4,9,'---')
		stdscr.addstr(5,8,'/   \\')
		stdscr.addstr(6,8,'|   |')
		stdscr.addstr(7,8,'\\   /')
		stdscr.addstr(8,9,'---')
	if missesRemaining == 10:
		stdscr.addstr(5,9,'O')
	if missesRemaining == 9:
		stdscr.addstr(5,11,'O')
	if missesRemaining == 8:
		stdscr.addstr(6,10,'>')
	if missesRemaining == 7:
		stdscr.addstr(7,9,'~~~')
	if missesRemaining == 6:
		stdscr.addstr(9,10,'|')
		stdscr.addstr(10,10,'|')
	if missesRemaining == 5:
		stdscr.addstr(10,9,'\\')
		stdscr.addstr(9,8,'\\')
	if missesRemaining == 4:
		stdscr.addstr(10,11,'/')
		stdscr.addstr(9,12,'/')
	if missesRemaining == 3:
		stdscr.addstr(11,10,'|')
		stdscr.addstr(12,10,'|')
		stdscr.addstr(13,10,'|')
	if missesRemaining == 2:
		stdscr.addstr(14,9,'/')
		stdscr.addstr(15,8,'/')
		stdscr.addstr(16,6,'_/')
	if missesRemaining == 1:
		stdscr.addstr(14,11,'\\')
		stdscr.addstr(15,12,'\\')
		stdscr.addstr(16,13,'\\_')
	
def playGame(stdscr):
	# Draw the gallows
	stdscr.addstr(1, 1, '┌────────┐')
	for i in range (2,4):
		stdscr.addstr(i, 10, '│')
	for i in range (2,20):
		stdscr.addstr(i, 1, '│')
	stdscr.addstr(20, 0, '─┴─')
	
	# Choose the word to guess
	wordNumber = randint(0, WORDLIST_SIZE - 1)
	with open('../wordlist.txt') as fp:
		for i, line in enumerate(fp):
			if i == wordNumber:
				wordToGuess = line.rstrip().upper()
				break;
	
	# Draw the guessing space
	for l in range(0, len(wordToGuess)):
		stdscr.addstr(10, 20 + (2 * l), '_ ')
	stdscr.addstr(12, 20, "Choose a letter: ")
	blanksRemaining = len(wordToGuess)
	missesRemaining = 11
	usedLetters = ''
	
	# Play the game
	while blanksRemaining > 0 and missesRemaining > 0:
		while True:
			ch = stdscr.getch()
			if ch == -1:
				continue
			ch = chr(ch).upper()
			break
		lettersFound = 0
		for l in range(0, len(wordToGuess)):
			if (wordToGuess[l] == ch and (255 & stdscr.inch(10, 20 + (2 * l))) == 95):
				lettersFound += 1
				stdscr.addstr(10, 20 + (2 * l), ch)
		blanksRemaining -= lettersFound
		if lettersFound == 0:
			drawFigure(stdscr, missesRemaining)
			missesRemaining -= 1
		usedLetters += ch
		stdscr.addstr(14, 20, usedLetters)
		stdscr.addstr(16, 20, f"Blanks Remaining: {blanksRemaining}  Misses Remaining: {missesRemaining}                 ")
	
	# Add a win/lose reaction
	if blanksRemaining == 0:
		stdscr.addstr(7, 9, '\\_/')
	if missesRemaining == 0:
		stdscr.addstr(7, 9, '/^\\')
		stdscr.addstr(5, 9, 'X X')
		
	for l in range(0, len(wordToGuess)):
		stdscr.addstr(10, 20 + (2 * l), wordToGuess[l])
		
	# New game?
	stdscr.addstr(1, 20, "Would you like to play again (Y/N)? ")
	while True:
		ch = stdscr.getch()
		if ch == -1:
			continue
		ch = chr(ch)
		stdscr.addstr(2, 20, ch)
		if ch not in ['Y', 'y', 'N', 'n']:
			continue
		newGame = ch
		break

	return newGame.lower() == 'y'

def main(stdscr):
	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
	curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
	curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_CYAN)
	curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

	stdscr.nodelay(True)
	stdscr.immedok(True)
	stdscr.clear()
	curses.curs_set(0)
	
	while playGame(stdscr):
		stdscr.clear()

curses.wrapper(main)