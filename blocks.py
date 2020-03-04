import pygame
import os

class Block(pygame.sprite.Sprite):
	def __init__(self, image, x, y, hitbox):
		super().__init__()
		self.image = image
		self.x = x
		self.y = y
		self.hitbox = pygame.Rect(x, y, 16, 16)
		self.image = pygame.image.load(os.path.join('sprites', image))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

