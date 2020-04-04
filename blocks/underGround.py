import pygame
from blocks.blocks import Block

class underGround(Block): #underground version of the ground block
	def __init__(self, x, y):
		super().__init__("undergroundGround.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
