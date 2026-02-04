import curses
class Card:
	value = '0'
	suite = 'X'
	color = 'white'
	colorPair = 0
	visible = False
	faceUp = False
	x = 0
	y = 0
	z = 0
	backsideChar = '/'
	def __init__(self, suite, value):
		self.suite = suite
		self.value = value

	def place(self, y, x, z, faceUp):
		self.x = x
		self.y = y
		self.z = z
		self.faceUp = faceUp
		return self

	def draw(self, window):
		window.addstr(self.y, self.x, '┌', curses.color_pair(self.colorPair))
		window.addstr(self.y, self.x + 3, '┐', curses.color_pair(self.colorPair))
		window.addstr(self.y + 4, self.x, '└', curses.color_pair(self.colorPair))
		window.addstr(self.y + 4, self.x + 3, '┘', curses.color_pair(self.colorPair))
		for h in range(1, 3):
			window.addstr(self.y, self.x + h, '─', curses.color_pair(self.colorPair))
			window.addstr(self.y + 4, self.x + h, '─', curses.color_pair(self.colorPair))
		for v in range(1, 4):
			window.addstr(self.y + v, self.x, '│', curses.color_pair(self.colorPair))
			window.addstr(self.y + v, self.x + 3, '│', curses.color_pair(self.colorPair))
		for h in range(1,3):
			for v in range(1,4):
				window.addstr(self.y + v, self.x + h, ' ', curses.color_pair(self.colorPair))
		if (self.faceUp):
			window.addstr(self.y + 1, self.x + 1, self.value, curses.color_pair(self.colorPair))
			window.addstr(self.y + 2, self.x + 1, self.suite, curses.color_pair(self.colorPair))
		else:
			for h in range(1,3):
				for v in range(1,4):
					window.addstr(self.y + v, self.x + h, self.backsideChar, curses.color_pair(self.colorPair))
		return self

	def flip(self, window):
		self.faceUp = not self.faceUp
		self.draw(window)
		return self