import pygame
from blocks.blocks import Block

class hiddenBlock(Block):
	def __init__(self, x, y):
		super().__init__("hiddenBlock.png", x, y, [16, 16])
