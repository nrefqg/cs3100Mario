import pygame
from blocks.blocks import Block

class stone(Block):
	def __init__(self, x, y):
		super().__init__("stone.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
		
