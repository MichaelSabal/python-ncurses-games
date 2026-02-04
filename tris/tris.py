import curses
from random import randint
from random import seed
from time import sleep, time
from math import floor

PIECE_TYPE_COUNT = 7

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
	if piece == 3:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32):
					return False
	if piece == 4:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32):
					return False
	if piece == 5:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32):
					return False
	if piece == 6:
		if pieceRotation == 0 or pieceRotation == 180:
			if (pieceAt[0] > 0 and (255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				(pieceAt[0] > 0 and (255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32):
					return False
	if piece == 7:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 0 and (255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if (pieceAt[0] > 0 and (255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] + 1, pieceAt[1] + 1)) > 32):
					return False

	return True
	
def canMoveLeft(stdscr, piece, pieceAt, pieceRotation):
	if pieceAt[0] <= 0:
		return True
	if piece == 1:
		if (255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32:
			return False
		if pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32:
			return False
	if piece == 2:
		if (255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32:
			return False
		if pieceRotation == 0 or pieceRotation == 180:
			if (pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 3 and (255 & stdscr.inch(pieceAt[0] - 3, pieceAt[1] - 1)) > 32):
					return False
	if piece == 3:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] - 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1]- 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32):
					return False
	if piece == 4:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] - 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] - 1)) > 32):
					return False
	if piece == 5:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] - 1)) > 32):
					return False
	if piece == 6:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32):
					return False
	if piece == 7:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] - 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] - 1)) > 32):
					return False
			
			
	return True
	
def canMoveRight(stdscr, piece, pieceAt, pieceRotation):
	if pieceAt[0] <= 0:
		return True
	if piece == 1:
		if (255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32:
			return False
		if pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32:
			return False
	if piece == 2:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] - 0, pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 3 and (255 & stdscr.inch(pieceAt[0] - 3, pieceAt[1] + 1)) > 32):
					return False
		elif pieceAt[1] > 6 or (255 & stdscr.inch(pieceAt[0], pieceAt[1] + 4)) > 32:
			return False
	if piece == 3:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 3)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 3)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 2)) > 32):
					return False
	if piece == 4:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 3)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 3)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 3)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 2)) > 32):
					return False
	if piece == 5:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 3)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 3)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 3)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 2)) > 32):
					return False
	if piece == 6:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 3)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 2)) > 32):
					return False
	if piece == 7:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 3)) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 1 and (255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32) or \
				(pieceAt[0] > 2 and (255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32):
					return False
	return True
	
def canRotate(stdscr, piece, pieceAt, pieceRotation):
	if piece == 1:
		return True
	if piece == 2:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] - 0, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 3, pieceAt[1])) > 32):
					return False
		else:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 0)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 3)) > 32):
					return False
	if piece == 3:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32):
					return False
	if piece == 4:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32):
					return False
	if piece == 5:
		if pieceRotation == 0:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32):
					return False
		if pieceRotation == 90:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32):
					return False
	if piece == 6:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 2)) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1] + 1)) > 32):
					return False
	if piece == 7:
		if pieceRotation == 0 or pieceRotation == 180:
			if ((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 2)) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32):
					return False
		if pieceRotation == 90 or pieceRotation == 270:
			if ((255 & stdscr.inch(pieceAt[0], pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1] + 1)) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 1, pieceAt[1])) > 32) or \
				((255 & stdscr.inch(pieceAt[0] - 2, pieceAt[1])) > 32):
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
						colorpair = curses.A_COLOR & ch
						stdscr.addstr(updateLine, j + upperLeft[1] + 1, chr(255 & ch), colorpair)
					updateLine -= 1
				stdscr.addstr(upperLeft[0] + 1, upperLeft[1] + 1, ''.join([' '] * width))
			else:
				stdscr.addstr(currentLine, upperLeft[1] + 1, ''.join([' '] * width))
		else:
			currentLine -= 1
	return removedLines
	
def undrawPiece(stdscr, piece, pieceAt, pieceRotation):
	BLANK = curses.color_pair(8)
	if piece == 1:
		if pieceAt[0] > 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], '  ', BLANK)
		if pieceAt[0] > 1:
			stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '  ', BLANK)
	if piece == 2:
		if pieceRotation == 0 or pieceRotation == 180:
			for y in range(0,4):
				if pieceAt[0] - y > 0:
					stdscr.addstr(pieceAt[0] - y, pieceAt[1], ' ', BLANK)
		else:
			for x in range(0,4):
				stdscr.addstr(pieceAt[0], pieceAt[1] + x, ' ', BLANK)
	if piece == 3:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], '   ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, ' ', BLANK)
		if pieceRotation == 90:
			stdscr.addstr(pieceAt[0], pieceAt[1], ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '  ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], ' ', BLANK)
		if pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '   ', BLANK)
		if pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '  ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1] + 1, ' ', BLANK)
	if piece == 4:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], '   ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 2, ' ', BLANK)
		if pieceRotation == 90:
			stdscr.addstr(pieceAt[0], pieceAt[1], '  ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], ' ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], ' ', BLANK)
		if pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1], ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '   ', BLANK)
		if pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, ' ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], '  ', BLANK)
	if piece == 5:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], '   ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], ' ', BLANK)
		if pieceRotation == 90:
			stdscr.addstr(pieceAt[0], pieceAt[1], '  ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, ' ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1] + 1, ' ', BLANK)
		if pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 2, ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '   ', BLANK)
		if pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1], ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], ' ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], '  ', BLANK)
	if piece == 6:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0 or pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, '  ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 0, '  ', BLANK)
		if pieceRotation == 90 or pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1], ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '  ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1] + 1, ' ', BLANK)
	if piece == 7:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0 or pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 0, '  ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, '  ', BLANK)
		if pieceRotation == 90 or pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, ' ', BLANK)
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '  ', BLANK)
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], ' ', BLANK)
	
def drawPiece(stdscr, piece, pieceAt, pieceRotation):
	if piece == 1:
		if pieceAt[0] > 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], '**', curses.color_pair(piece))
		if pieceAt[0] > 1:
			stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '**', curses.color_pair(piece))
	if piece == 2:
		if pieceRotation == 0 or pieceRotation == 180:
			for y in range(0,4):
				if pieceAt[0] - y > 0:
					stdscr.addstr(pieceAt[0] - y, pieceAt[1], '=', curses.color_pair(piece))
		else:
			for x in range(0,4):
				if pieceAt[0] > 0:
					stdscr.addstr(pieceAt[0], pieceAt[1] + x, '=', curses.color_pair(piece))
	if piece == 3:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], 'TTT', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, 'T', curses.color_pair(piece))
		if pieceRotation == 90:
			stdscr.addstr(pieceAt[0], pieceAt[1], 'T', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], 'TT', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], 'T', curses.color_pair(piece))
		if pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, 'T', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], 'TTT', curses.color_pair(piece))
		if pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, 'T', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], 'TT', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1] + 1, 'T', curses.color_pair(piece))
	if piece == 4:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], 'LLL', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 2, 'L', curses.color_pair(piece))
		if pieceRotation == 90:
			stdscr.addstr(pieceAt[0], pieceAt[1], 'LL', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], 'L', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], 'L', curses.color_pair(piece))
		if pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 0, 'L', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], 'LLL', curses.color_pair(piece))
		if pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, 'L', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, 'L', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], 'LL', curses.color_pair(piece))
	if piece == 5:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0:
			stdscr.addstr(pieceAt[0], pieceAt[1], 'JJJ', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 0, 'J', curses.color_pair(piece))
		if pieceRotation == 90:
			stdscr.addstr(pieceAt[0], pieceAt[1], 'JJ', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, 'J', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1] + 1, 'J', curses.color_pair(piece))
		if pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 2, 'J', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], 'JJJ', curses.color_pair(piece))
		if pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1], 'J', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], 'J', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], 'JJ', curses.color_pair(piece))
	if piece == 6:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0 or pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, '22', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 0, '22', curses.color_pair(piece))
		if pieceRotation == 90 or pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1], '2', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '22', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1] + 1, '2', curses.color_pair(piece))
	if piece == 7:
		if pieceAt[0] <= 0:
			return
		if pieceRotation == 0 or pieceRotation == 180:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 0, '55', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1] + 1, '55', curses.color_pair(piece))
		if pieceRotation == 90 or pieceRotation == 270:
			stdscr.addstr(pieceAt[0], pieceAt[1] + 1, '5', curses.color_pair(piece))
			if pieceAt[0] > 1:
				stdscr.addstr(pieceAt[0] - 1, pieceAt[1], '55', curses.color_pair(piece))
			if pieceAt[0] > 2:
				stdscr.addstr(pieceAt[0] - 2, pieceAt[1], '5', curses.color_pair(piece))

def playGame(stdscr):
	maxLines = curses.LINES
	maxColumns = curses.COLS
	maxBoardLines = min(20, maxLines - 2)
	maxBoardColumns = min(10, maxColumns - 2)
	seed() # from random
	
	linesCleared = 0
	score = 0
	round = 1
	upperLeft = [0, 0]
	
	initBoard(stdscr, upperLeft[0], upperLeft[1], maxBoardLines, maxBoardColumns)
	if maxColumns - maxBoardColumns > 20:
		stdscr.addstr(2, maxBoardColumns + 3, "Move piece: L/R Arrow")
		stdscr.addstr(3, maxBoardColumns + 3, "Rotate: Up Arrow or Space")
		stdscr.addstr(4, maxBoardColumns + 3, "Drop: Down Arrow or Enter")
		stdscr.addstr(5, maxBoardColumns + 3, "Quit: Esc or X or Q")
	gameOver = False
	pieceAt = [-1, -1]
	nextPiece = -1
	thisPiece = 1
	while nextPiece < 1 or nextPiece > PIECE_TYPE_COUNT:
		nextPiece = randint(0,10 * PIECE_TYPE_COUNT)
		nextPiece = floor(nextPiece / 10) + 1
	pieceRotation = 0
	lastVerticalTime = time()
	while not gameOver:
		if maxColumns - maxBoardColumns > 20:
			stdscr.addstr(7, maxBoardColumns + 3, f"Round: {round}")
			stdscr.addstr(9, maxBoardColumns + 3, f"Score: {score}")
			stdscr.addstr(11, maxBoardColumns + 3, f"Lines: {linesCleared}")
		if pieceAt[0] == -1:
			thisPiece = nextPiece
			# Multiply max integer by 10 to better balance the mix of pieces
			nextPiece = -1
			while nextPiece < 1 or nextPiece > PIECE_TYPE_COUNT:
				nextPiece = randint(0,10 * PIECE_TYPE_COUNT)
				nextPiece = floor(nextPiece / 10) + 1
			pieceAt = [0, 4]
			pieceRotation = 0
			if not canMoveDown(stdscr, thisPiece, pieceAt, pieceRotation):
				gameOver = True
				stdscr.addstr(13, maxBoardColumns + 3, "GAME OVER")
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
		if (ch == 259 or ch == 32): # and canMoveRight(stdscr, thisPiece, pieceAt, (pieceRotation + 90) % 360):
			undrawPiece(stdscr, thisPiece, pieceAt, pieceRotation)
			if canRotate(stdscr, thisPiece, pieceAt, (pieceRotation + 90) % 360):
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