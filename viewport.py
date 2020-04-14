import pygame
FONT_COLOR = (255, 255, 255)

class Viewport:
    """
    TODO: Update documentation
    Represents the viewport of the game so it includes the camera
    and the GUI.
    """
    def __init__(self, screen_width, screen_height):
        """
        """
        self.offsetX = 0
        self.offsetY = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
        # Intialize fonts
        pygame.font.init()
        self.myfont = pygame.font.SysFont('freesansbold.ttf', 24)

    def reset(self):
        """
        Fills the screen with blank blue to reset the frame.
        """
        # TODO: Make this based upon a constant
        self.screen.fill((146, 244, 255))

    def in_frame(self, sprite_x, sprite_y):
        """
        Checks to see if the sprite is in the viewport. Used to figure out if
        we should even try blitting the sprite
        """
        # Check to see if x and y position is in the viewport x range
        if sprite_x >= self.offsetX and sprite_x <= self.screen_width + self.offsetX:
            if sprite_y >= self.offsetY and sprite_y <= self.screen_height + self.offsetY:
                return True
        return False

    def check_pos(self, player_location):
        """
        Checks Mario's position to determine whether or not the viewport
        camera needs to be shifted
        """
        if player_location[0] > (self.screen_width / 2) + self.offsetX:
            #diff = (self.screen_width / 2) + self.offsetX - player_location[0]
            # 1 is currently the player speed.
            # TODO: Player speed be a passed in parameter soon
            self.offsetX += 6

    def render_ui(self):
        '''
        Takes in level information and renders it out
        '''
        test_world_number = 1
        test_world_checkpoint = 5 
        mario_label = self.myfont.render('MARIO', True, FONT_COLOR)
        world_label = self.myfont.render('WORLD', True, FONT_COLOR)
        time_label = self.myfont.render('TIME', True, FONT_COLOR)
        score = self.myfont.render('000000', True, FONT_COLOR)
        coin = self.myfont.render('0x00', True, FONT_COLOR)
        level = self.myfont.render('%s - %x' % (test_world_number, test_world_checkpoint), True, FONT_COLOR)
        time = self.myfont.render('999', True, FONT_COLOR)

        self.screen.blit(mario_label, (80, 20))
        self.screen.blit(world_label, (240, 20))
        self.screen.blit(time_label, (380, 20))
        self.screen.blit(score, (80, 40))
        self.screen.blit(coin, (160, 40))
        self.screen.blit(level, (255, 40))
        self.screen.blit(time, (385, 40))

    def render_sprites(self, player_sprite, player_location, enemies, blocks, pipes):
        """
        Takes in sprites and locations of the player, enemy, blocks, and pipe
        blocks and renders to the viewport if the sprites are in the viewport
        position.
        """
        self.check_pos(player_location)

        # Render player sprite
        self.screen.blit(player_sprite, [player_location[0] - self.offsetX, player_location[1]])

        # Render potential enemies
        if enemies:
            for enemy in enemies:
                if self.in_frame(enemy.rect.x, enemy.rect.y):
                    self.screen.blit(enemy.image, [enemy.rect.x - self.offsetX, enemy.rect.y])

        # Render potential blocks
        if blocks:
            for block in blocks:
                if self.in_frame(block.rect.x, block.rect.y):
                    self.screen.blit(block.image, [block.rect.x - self.offsetX, block.rect.y])

        # Render potential pipes
        if pipes:
            for pipe in pipes:
                if self.in_frame(pipe.rect.x, pipe.rect.y):
                    self.screen.blit(pipe.image, [pipe.rect.x - self.offsetX, pipe.rect.y])
