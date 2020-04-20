import pygame
from blocks.blocks import Block

class multiCoin(Block):
	self.count = 5
	
	def __init__(self, x, y):
		super().__init__("powerBlock.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32

	def disabled(self, x, y):
		super().__init__("disabledBlock.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
		
	def decrementCount(self):
		if self.count > 0:
			self.count = self.count - 1
			return True
		else:
			return False
