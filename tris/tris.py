import curses
from random import randint
from time import sleep, time
from math import floor

PIECE_TYPE_COUNT = 2

def initBoard(stdscr, y, x, h, w):
	stdscr.clear()
	stdscr.addstr(y, x, '╔')
	stdscr.addstr(y, x+w+1, '╗')
	stdscr.addstr(y+h+1, x, '╚')
	stdscr.addstr(y+h+1, x+w+1, '╝')
	for i in range(x+1, x+w+1):
		stdscr.addstr(y, i, '═')
		stdscr.addstr(y+h+1, i, '═')
	for i in range(y+1, y+h+1):
		stdscr.addstr(i, x, '║')
		stdscr.addstr(i, x+w+1, '║')

def canMoveDown(stdscr, piece, pieceAt, pieceRotation):
	if piece == 1:
		if (255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32:
			return False
		if (255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32:
			return False
	if piece == 2:
		if (255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32:
			return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 3)) > 32):
					return False
			
	return True
	
def canMoveLeft(stdscr, piece, pieceAt, pieceRotation):
	if piece == 1:
		if (255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32:
			return False
		if (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32:
			return False
	if piece == 2:
		if (255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32:
			return False
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] - 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 3, pieceAt[1] - 1)) > 32):
					return False
			
			
	return True
	
def canMoveRight(stdscr, piece, pieceAt, pieceRotation):
	if piece == 1:
		if (255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32:
			return False
		if (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32:
			return False
	if piece == 2:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] - 0, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 3, pieceAt[1] + 1)) > 32):
					return False
		elif pieceAt[1] > 6 or (255 & stdscr.inch(pieceAt[0], pieceAt[1] + 4)) > 32:
			return False

	return True
	
def checkLines(stdscr, upperLeft, size):
	removedLines = 0
	height = size[0]
	width = size[1]
	currentLine = upperLeft[0] + height
	while currentLine > upperLeft[0]:
		lineFilled = True
		for x in range(upperLeft[1] + 1, upperLeft[1] + width + 2):
			if (255 & stdscr.inch(currentLine, x)) == 32:
				lineFilled = False
				break
		if lineFilled:
			removedLines += 1
			if currentLine > upperLeft[0] + 1:
				updateLine = currentLine
				while updateLine > upperLeft[0] + 1:
					for j in range(0, width):
						ch = stdscr.inch(updateLine - 1, upperLeft[1] + j + 1)
						colorpair = curses.pair_content(ch & curses.A_COLOR)
						stdscr.addstr(updateLine, j + upperLeft[1] + 1, chr(255 & ch), curses.color_pair(colorpair[1]))
					updateLine -= 1
				stdscr.addstr(upperLeft[0] + 1, upperLeft[1] + 1, ''.join([' '] * width))
			else:
				stdscr.addstr(currentLine, upperLeft[1] + 1, ''.join([' '] * width))
		else:
			currentLine -= 1
	return removedLines
	
def undrawPiece(stdscr, piece, pieceAt, pieceRotation):
	if piece == 1:
		if pieceAt[0] > 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], '  ')
		if pieceAt[0] > 1:
			stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '  ')
	if piece == 2:
		if pieceRotation == 0 or pieceRotation == 180:
			for y in range(0,4):
				if pieceAt[0] - y > 0:
					stdscr.addstr(pieceAt[0] - y, pieceAt[1], ' ')
		else:
			for x in range(0,4):
				stdscr.addstr(pieceAt[0], pieceAt[1] + x, ' ')
	
def drawPiece(stdscr, piece, pieceAt, pieceRotation):
	if piece == 1:
		if pieceAt[0] > 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], '**')
		if pieceAt[0] > 1:
			stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '**')
	if piece == 2:
		if pieceRotation == 0 or pieceRotation == 180:
			for y in range(0,4):
				if pieceAt[0] - y > 0:
					stdscr.addstr(pieceAt[0] - y, pieceAt[1], '=')
		else:
			for x in range(0,4):
				stdscr.addstr(pieceAt[0], pieceAt[1] + x, '=')

def playGame(stdscr):
	maxLines = curses.LINES
	maxColumns = curses.COLS
	maxBoardLines = min(20, maxLines - 2)
	maxBoardColumns = min(10, maxColumns - 2)
	
	linesCleared = 0
	score = 0
	round = 1
	upperLeft = [0, 0]
	
	initBoard(stdscr, upperLeft[0], upperLeft[1], maxBoardLines, maxBoardColumns)
	gameOver = False
	pieceAt = [-1, -1]
	nextPiece = 1
	thisPiece = 1
	pieceRotation = 0
	lastVerticalTime = time()
	while not gameOver:
		if maxColumns - maxBoardColumns > 20:
			stdscr.addstr(5, maxBoardColumns + 3, f"Round: {round}")
			stdscr.addstr(7, maxBoardColumns + 3, f"Score: {score}")
			stdscr.addstr(9, maxBoardColumns + 3, f"Lines: {linesCleared}")
		if pieceAt[0] == -1:
			thisPiece = nextPiece
			# Add one to the max integer to better balance the mix of pieces
			nextPiece = -1
			while nextPiece < 1 or nextPiece > PIECE_TYPE_COUNT:
				nextPiece = randint(1,PIECE_TYPE_COUNT + 1)
			pieceAt = [0, 4]
			pieceRotation = 0
			if not canMoveDown(stdscr, thisPiece, pieceAt, pieceRotation):
				gameOver = True
				stdscr.addstr(11, maxBoardColumns + 3, "GAME OVER")
				break
			score += 10
		if (time() - lastVerticalTime) > (10 / (round + 5)):
			if canMoveDown(stdscr, thisPiece, pieceAt, pieceRotation):
				undrawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
				pieceAt[0] += 1
				drawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
				score += 1
				lastVerticalTime = time()
			else:
				pieceAt = [-1, -1]
				linesRemoved = checkLines(stdscr, upperLeft, [maxBoardLines, maxBoardColumns])
				linesCleared += linesRemoved
				score += (round * 100 * linesRemoved)
				round = 1 + floor(linesCleared / maxBoardLines)
		ch = stdscr.getch()
		if ch > -1:
			stdscr.addstr(13, 20, f"{ch}    ")
		if ch == 260 and canMoveLeft(stdscr, thisPiece, pieceAt, pieceRotation):
			undrawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
			pieceAt[1] -= 1
			drawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
		if ch == 261 and canMoveRight(stdscr, thisPiece, pieceAt, pieceRotation):
			undrawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
			pieceAt[1] += 1
			drawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
		if (ch == 258 or ch == 10) and canMoveDown(stdscr, thisPiece, pieceAt, pieceRotation):
			undrawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
			pieceAt[0] += 1
			drawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
			score += 1
		if (ch == 259 or ch == 32) and canMoveRight(stdscr, thisPiece, pieceAt, (pieceRotation + 90) % 360):
			undrawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
			pieceRotation = (pieceRotation + 90) % 360
			drawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
		if ch == 27 or (ch > 32 and chr(ch) in ['q','Q','x','X']):
			gameOver = True
		

	stdscr.addstr(maxLines - 1, 0, "Would you like to play again (Y/N)? ")
	while True:
		ch = stdscr.getch()
		if ch == -1:
			continue
		ch = chr(ch)
		stdscr.addstr(maxLines - 1, 36, ch)
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