#import pygame
from blocks.blocks import Block

class leftPipe(Block):
	def __init__(self, x, y):
		super().__init__("leftPipe.png", x, y, [16, 16])

class rightPipe(Block):
	def __init__(self, x, y):
		super().__init__("rightPipe.png", x, y, [16, 16])

class midPipe(Block):
	def __init__(self, x, y):
		super().__init__("midPipe.png", x, y, [16, 16])
