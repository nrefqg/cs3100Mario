import pygame
from blocks.blocks import Block

class underStone(Block): #undergound verson of stone blocks
	def __init__(self, x, y):
		super().__init__("undergroundStone.png", x, y)
		self.xHitRight = x+32
		self.xHitBottom = y+32
