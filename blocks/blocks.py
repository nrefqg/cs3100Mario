import pygame
import os


class Block(pygame.sprite.Sprite):
	def __init__(self, image, x, y):
		super().__init__()
		self.image = image
		self.x = x
		self.y = y
		self.image = pygame.image.load(os.path.join('sprites', image)) #Allows sub-classes to access sprite folder easily
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.isdisabled = False
