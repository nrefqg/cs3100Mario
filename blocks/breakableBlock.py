import pygame
from blocks.blocks import Block

class breakableBlock(Block):
	def __init__(self, x, y):
		super().__init__("breakableBlock.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32

	def destroy(self, sprite_group):
		sprite_group.remove(self)