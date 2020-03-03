import pygame

class Block(pygame.sprite.Sprite):
	def __init__(self, image, x, y, hitbox):
		super().__init__()
		self.image = image
		self.x = x
		self.y = y
		self.hitbox = Rect(x, y, 64, 64)
