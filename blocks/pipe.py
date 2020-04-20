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


class topPipeLeft(Block):
	def __init__(self, x, y):
		super().__init__("top_pipe_left.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32

class topPipeRight(Block):
	def __init__(self, x, y):
		super().__init__("top_pipe_right.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32

class entranceLeft(Block):
	def __init__(self, x, y):
		super().__init__("top_pipe_left.png", x, y)

class entranceRight(Block):
	def __init__(self, x, y):
		super().__init__("top_pipe_right.png", x, y)

class exitLeft(Block):
	def __init__(self, x, y):
		super().__init__("top_pipe_left.png", x, y)

class exitRight(Block):
	def __init__(self, x, y):
		super().__init__("top_pipe_right.png", x, y)

class hiddenPipe(Block):
	def __init__(self, x, y):
		super().__init__("hiddenPipe.png", x, y)

