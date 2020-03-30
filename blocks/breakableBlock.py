import pygame
from blocks.blocks import Block

class breakableBlock(Block):
	def __init__(self, x, y):
		super().__init__("breakableBlock.png", x, y, [16, 16])
