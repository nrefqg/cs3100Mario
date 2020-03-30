from blocks.blocks import Block


class leftPipe(Block):
	def __init__(self, x, y):
		super().__init__("leftPipe.png", x, y)


class rightPipe(Block):
	def __init__(self, x, y):
		super().__init__("rightPipe.png", x, y)


class midPipe(Block):
	def __init__(self, x, y):
		super().__init__("midPipe.png", x, y)
