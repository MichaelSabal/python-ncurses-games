import curses
from random import randint
from time import sleep
from math import floor

def chooseSecret(stdscr):
	stdscr.addstr(0, 0, "Press the number of the slot repeatedly to change the color.")
	stdscr.addstr(1, 0, "Press <Enter> to lock it in.")
	stdscr.addstr(2, 0, "  [ 1 ]  [ 2 ]  [ 3 ]  [ 4 ]")
	secret = [-1, -1, -1, -1]
	while True:
		ch = stdscr.getch()
		if ch == -1:
			continue
		if ch == 10 and -1 not in secret:
			return secret
		if ch >= 49 and ch <= 52:
			index = ch - 49
			secret[index] = (secret[index] + 1) % 6
			if secret[index] == 0:
				secret[index] = 6
			display = index + 1
			stdscr.addstr(2, 3 + (index * 7), f" {display} ", curses.color_pair(secret[index]))

def makeComputerSecret():
	return [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
	
def getHumanGuess(stdscr, turn):
	guess = [-1, -1, -1, -1]
	while True:
		ch = stdscr.getch()
		if ch == -1:
			continue
		if ch == 10 and -1 not in guess:
			return guess
		if ch >= 49 and ch <= 52:
			index = ch - 49
			guess[index] = (guess[index] + 1) % 6
			if guess[index] == 0:
				guess[index] = 6
			display = index + 1
			stdscr.addstr(turn, 5 + (index * 5), f" {display} ", curses.color_pair(guess[index]))

def getComputerGuess(stdscr, turn, possibleColors, computerGuessHistory):
	if turn == 1:
		n1 = randint(1,6)
		n2 = randint(1,6)
		guess = [n1, n2, n1, n2]
	elif len(computerGuessHistory) > 0 and computerGuessHistory[-1][-1] + computerGuessHistory[-1][-2] == 4:
		guess = random.shuffle(computerGuessHistory[-1][0:3])
	else:
		guess = [
			randint(0,len(possibleColors)-1),
			randint(0,len(possibleColors)-1),
			randint(0,len(possibleColors)-1),
			randint(0,len(possibleColors)-1)
		]
		for k in range(0,4):
			guess[k] = possibleColors[guess[k]]
	for i in range(0,4):
		display = i + 1
		stdscr.addstr(turn, 45 + (i * 5), f" {display} ", curses.color_pair(guess[i]))
	return guess
	
def checkGuess(guess, actual):
	bulls = 0
	cows = 0
	claimed = [False, False, False, False]
	for i in range(0,4):
		if guess[i] == actual[i]:
			claimed[i] = True
			bulls = bulls + 1
	for i in range(0,4):
		if claimed[i]:
			continue
		for j in range(0,4):
			if not claimed[j] and guess[i] == actual[j]:
				claimed[j] = True
				cows = cows + 1
				break
	return bulls, cows
	
def playGame(stdscr):
	userSecret = chooseSecret(stdscr)
	computerSecret = makeComputerSecret()
	stdscr.clear()
	stdscr.addstr(0,11,"Your guesses")
	stdscr.addstr(0,51,"Computer guesses")
	for i in range(1,13):
		stdscr.addstr(i, 0, '{: >2}'.format(i))
		stdscr.addstr(i, 4, "[ 1 ][ 2 ][ 3 ][ 4 ] [X][X][X][X]")
		stdscr.addstr(i, 44, "[ 1 ][ 2 ][ 3 ][ 4 ] [X][X][X][X]")

	possibleColors = [1, 2, 3, 4, 5, 6]
	computerGuessHistory = []
	complete = False
	turn = 1
	while not complete:
		guess = getHumanGuess(stdscr, turn)
		bulls, cows = checkGuess(guess, computerSecret)
		if bulls == 4:
			stdscr.addstr(15, 0, "Congratulations! You win")
			complete = True
		pos = 26
		while bulls > 0:
			stdscr.addstr(turn, pos, '*', curses.color_pair(100))
			bulls = bulls - 1
			pos = pos + 3
		while cows > 0:
			stdscr.addstr(turn, pos, '+', curses.color_pair(99))
			cows = cows - 1
			pos = pos + 3
		while pos <= 35:
			stdscr.addstr(turn, pos, ' ')
			pos = pos + 3
		guess = getComputerGuess(stdscr, turn, possibleColors, computerGuessHistory)
		bulls, cows = checkGuess(guess, userSecret)
		historyguess = list(guess)
		historyguess.append(bulls)
		historyguess.append(cows)
		computerGuessHistory.append(historyguess)
		if bulls == 4:
			stdscr.addstr(15, 0, "Sorry to disappoint you, but I win")
			complete = True
		elif bulls == 0 and cows == 0:
			#stdscr.addstr(17, 0, "Removing ")
			for i in range(0, 4):
				val = guess[i]
				#stdscr.addstr(17, 9+i, f"{val}")
				for j in range(0,len(possibleColors)):
					if guess[i] == possibleColors[j]:
						possibleColors.remove(possibleColors[j])
						break
			#stdscr.addstr(17, 30, "          ")
			#for k in range(0,len(possibleColors)):
				#pki = possibleColors[k]
				#stdscr.addstr(17, 30+k, f"{pki}") 
		elif bulls + cows == 4:
			possibleColors = guess
		pos = 66
		while bulls > 0:
			stdscr.addstr(turn, pos, '*', curses.color_pair(100))
			bulls = bulls - 1
			pos = pos + 3
		while cows > 0:
			stdscr.addstr(turn, pos, '+', curses.color_pair(99))
			cows = cows - 1
			pos = pos + 3
		while pos <= 75:
			stdscr.addstr(turn, pos, ' ')
			pos = pos + 3

		turn = turn + 1
		if turn > 12:
			stdscr.addstr(15, 0, "That was tough! Nobody wins.")
			complete = True
		
	stdscr.addstr(16, 0, "Would you like to play again (Y/N)? ")
	while True:
		ch = stdscr.getch()
		if ch == -1:
			continue
		ch = chr(ch)
		stdscr.addstr(16, 36, ch)
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
	curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK)
	curses.init_pair(99, curses.COLOR_BLACK, curses.COLOR_WHITE) # Cow
	curses.init_pair(100, curses.COLOR_YELLOW, curses.COLOR_RED) # Bull

	stdscr.nodelay(True)
	stdscr.immedok(True)
	stdscr.clear()
	curses.curs_set(0)
	
	while playGame(stdscr):
		stdscr.clear()


curses.wrapper(main)