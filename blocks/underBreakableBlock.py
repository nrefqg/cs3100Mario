import pygame
from blocks.blocks import Block

class underBreakableBlock(Block): #underground version of the breakable blocks
	def __init__(self, x, y):
		super().__init__("undergroundBreakableBlock.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
