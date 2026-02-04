import curses
import os
from random import randint
from random import seed
from time import sleep, time
from math import floor, log10
from Deck import Deck

def bestValue(hand):
		sum = 0
		aces = 0
		for card in hand.cardList:
			if card.value == 'A':
				aces += 1
			elif card.value == '10' or card.value == 'J' or card.value == 'Q' or card.value == 'K':
				sum += 10
			else:
				sum += (ord(card.value) - 48)
		if aces == 0:
			return sum
		if sum >= (12 - aces):
			return sum + aces
		return sum + 11 + (aces - 1)
	
def playGame(stdscr, computerMoney, humanMoney):
	if computerMoney <= 0:
		computerMoney = 100
	if humanMoney <= 0:
		humanMoney = 100
	drawPile = Deck()
	drawPile.makeDeck(52).shuffle()
	humanHand = Deck()
	computerHand = Deck()
	stdscr.addstr(0, 0, f"Computer: ${computerMoney}")
	stdscr.addstr(0, 20, f"Human: ${humanMoney}")
	stdscr.addstr(1, 0, "Your hand:")
	humanHand.addToBottom(drawPile.takeFromTop().place(2,2,0,True).draw(stdscr))
	humanHand.addToBottom(drawPile.takeFromTop().place(2,8,0,True).draw(stdscr))
	humanSum = bestValue(humanHand)
	stdscr.addstr(7, 0, "Computer hand:")
	computerHand.addToBottom(drawPile.takeFromTop().place(8,2,0,False).draw(stdscr))
	computerHand.addToBottom(drawPile.takeFromTop().place(8,8,0,True).draw(stdscr))
	computerSum = bestValue(computerHand)
	stdscr.addstr(20, 0, f"Place your bet (max ${humanMoney}): $")
	betstr = ''
	while True:
		stdscr.addstr(20, 26 + floor(log10(humanMoney)), betstr)
		betchar = -1
		while betchar < 48 or betchar > 57:
			betchar = stdscr.getch()
			if betchar == 10 or betchar == 13:
				break
		if betchar >= 48 and betchar <= 57:
			betstr = betstr + chr(betchar)
			continue
		try:
			bet = int(betstr)
		except:
			continue
		if bet > -1 and bet <= humanMoney:
			break
	roundInProgress = humanSum < 21 and computerSum < 21
	humanResult = 1 if humanSum == 21 else 0
	computerResult = 1 if computerSum == 21 else 0
	while roundInProgress:
		stdscr.addstr(20, 0, ' '*curses.COLS)
		stdscr.addstr(20, 0, "(H)it or (P)ass? ")
		while True:
			ch = stdscr.getch()
			if ch == -1:
				continue
			ch = chr(ch)
			stdscr.addstr(20, 20, ch)
			if ch not in ['H', 'h', 'P', 'p']:
				continue
			action = ch.lower()
			break
		if action == 'h':
			humanHand.addToBottom(drawPile.takeFromTop().place(2,2+(6*humanHand.size()),0,True).draw(stdscr))
			sum = bestValue(humanHand)
			if sum > 21:
				roundInProgress = False
				humanResult = -1
			elif sum == 21:
				roundInProgress = False
				humanResult = 1
		computerSum = bestValue(computerHand)
		if computerSum < 17:
			computerHand.addToBottom(drawPile.takeFromTop().place(8,2+(6*computerHand.size()),0,True).draw(stdscr))
			computerSum = bestValue(computerHand)
			if computerSum > 21:
				roundInProgress = False
				computerResult = -1
			elif computerSum == 21:
				roundInProgress = False
				computerResult = 1
		elif action == 'p':
			roundInProgress = False
	
	computerHand.revealAll(stdscr)
	if humanResult == 0 and computerResult == 0:
		humanSum = bestValue(humanHand)
		computerSum = bestValue(computerHand)
		if humanSum > computerSum:
			humanResult = 1
			computerResult = -1
		if computerSum > humanSum:
			computerSum = 1
			humanSum = -1
	elif humanResult == 0:
		humanResult = -1 * computerResult
	elif computerResult == 0:
		computerResult = -1 * humanResult
			
	computerMoney += (100 * computerResult)
	humanMoney += (bet * humanResult)
	stdscr.addstr(0, 0, ' '*curses.COLS)
	stdscr.addstr(0, 0, f"Computer: ${computerMoney}")
	stdscr.addstr(0, 20, f"Human: ${humanMoney}")
	if humanResult > 0:
		stdscr.addstr(1, 0, '*** WINNER ***', curses.color_pair(2))
	if computerResult > 0:
		stdscr.addstr(7, 0, '*** WINNER ***', curses.color_pair(2))
	if humanResult < 0:
		stdscr.addstr(1, 0, '   ! BUST !   ', curses.color_pair(1))
	if computerResult < 0:
		stdscr.addstr(7, 0, '   ! BUST !   ', curses.color_pair(1))

	stdscr.addstr(curses.LINES - 1, 0, "Would you like to play again (Y/N)? ")
	while True:
		ch = stdscr.getch()
		if ch == -1:
			continue
		ch = chr(ch)
		stdscr.addstr(curses.LINES - 1, 36, ch)
		if ch not in ['Y', 'y', 'N', 'n']:
			continue
		newGame = ch
		break

	return newGame.lower() == 'y', computerMoney, humanMoney

def main(stdscr):
	computerMoney = 1000
	humanMoney = 1000

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
	
	while True:
		newGame, computerMoney, humanMoney = playGame(stdscr, computerMoney, humanMoney)
		if not newGame:
			break
		stdscr.clear()

curses.wrapper(main)
