#import pygame
from blocks.blocks import Block

class redBlock(Block):
	def __init__(self, x, y):
		super().__init__("redBlock.png", x, y, [16, 16])
