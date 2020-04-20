import pygame
from blocks.blocks import Block

class powerBlock(Block):
	def __init__(self, x, y):
		super().__init__("powerBlock.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
		self.enabled = True

	def disabled(self, x, y):
		super().__init__("disabledBlock.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
		self.enabled = False
