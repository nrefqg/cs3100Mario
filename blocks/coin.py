import pygame
import os
from blocks.blocks import Block

class coin(Block):
	def __init__(self, x, y):
		super().__init__("Coin1.png", x, y)
		self.yHitBottom = y+32
		self.xHitRight = x+32
		self.animate = [] #Method to provide coin with an animation
		self.animate.append(pygame.image.load(os.path.join('sprites/Coin1.png')))
		self.animate.append(pygame.image.load(os.path.join('sprites/Coin3.png')))
		self.animate.append(pygame.image.load(os.path.join('sprites/Coin5.png')))
		self.animate.append(pygame.image.load(os.path.join('sprites/Coin2.png')))
		self.animate.append(pygame.image.load(os.path.join('sprites/Coin4.png')))
		self.animate.append(pygame.image.load(os.path.join('sprites/Coin5.png')))
		self.index = 0
		self.image = self.animate[self.index]

	def update(self): #Animation of the coin
		self.index += 1
		if self.index >= len(self.animate):
			self.index = 0
		self.image = self.animate[self.index]

	def destroy(self, sprite_group): #Removes coin when picked up
		sprite_group.remove(self)

