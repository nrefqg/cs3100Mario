from blocks.blocks import Block


class leftPipe(Block):
	def __init__(self, x, y):
		super().__init__("leftPipe.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32


class rightPipe(Block):
	def __init__(self, x, y):
		super().__init__("rightPipe.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32


class topPipe(Block):
	def __init__(self, x, y):
		super().__init__("topPipe.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32

class hiddenPipe(Block):
	def __init__(self, x, y):
		super().__init__("hiddenPipe.png", x, y)

