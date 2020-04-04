import pygame
from blocks.blocks import Block

class ground(Block):
	def __init__(self, x, y):
		super().__init__("ground.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
