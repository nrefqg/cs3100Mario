import pygame
from blocks.blocks import Block

class flagpole(Block):
	def __init__(self, x, y):
		super().__init__("flagpole.png", x, y)
		self.xHitRight = x+4
		self.xHitBottom = y+4

class flag(Block):
	def __init__(self, x, y):
		super().__init__("flag.png", x, y)
		
