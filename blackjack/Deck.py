from Card import Card
import random
class Deck:
	cardList = []
	def __init__(self):
		self.cardList = []

	def makeDeck(self, size):
		suites = ['H','S','D','C']
		cards = ['A','2','3','4','5','6','7','8','9','J','Q','K']
		for suite in suites:
			for card in cards:
				self.cardList.append(Card(suite, card))
		return self
				
	def shuffle(self):
		random.shuffle(self.cardList)
		return self
		
	def takeFromTop(self):
		if len(self.cardList) == 0:
			return Nothing
		topCard = self.cardList[0]
		self.cardList = self.cardList[1:]
		return topCard
		
	def isEmpty(self):
		return len(self.cardList) == 0
		
	def addToTop(self, card):
		self.cardList.insert(0, card)
		return self
		
	def addToBottom(self, card):
		self.cardList.append(card)
		return self
		
	def size(self):
		return len(self.cardList)
		
	def revealAll(self, stdscr):
		for card in self.cardList:
			if not card.faceUp:
				card.flip(stdscr)