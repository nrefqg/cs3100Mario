import pygame
import sys
FONT_COLOR = (255, 255, 255)

class Viewport:
    """
    Class that controls the camera and UI elements for the game.
    Render any sprites, game information, etc here.
    """
    def __init__(self, screen_width, screen_height):
        """
        Constructor for the viewport.
        :param screen_width: Integer for the width of the game window
        :param screen_height: Integer for the height of the game window
        """
        self.offsetX = 0
        self.offsetY = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
        # Intialize fonts
        pygame.font.init()
        self.myfont = pygame.font.SysFont('freesansbold.ttf', 24)

    def game_menu(self):
        """
        Loads a main menu loop that will only end when the player decides to
        start the game or quit
        :return: None
        """
        menu_image = pygame.image.load('start_menu.png')
        self.screen.blit(menu_image, (0, 0))
        pygame.display.update()
        while True:
            # Respond to player input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()  # Stop pygame
                    sys.exit()  # Stop script

                # Respond to player keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                        pygame.quit()  # Stop pygame
                        sys.exit()  # Stop script

    def reset(self, sky_color):
        """
        Fills the screen with a color to reset all the elements.
        :param sky_color: 3-element tuple representing RGB values
        :return: None
        """
        # TODO: Make this based upon a constant
        self.screen.fill(sky_color)

    def in_frame(self, sprite_x, sprite_y):
        """
        Checks to see if the sprite is in the viewport.
        :param sprite_x: Int representing sprite x position
        :param sprite_y: Int representing sprite y position
        :return: None
        """
        # Check to see if x and y position is in the viewport x range
        if sprite_x >= self.offsetX - 32 and sprite_x <= self.screen_width + self.offsetX + 32:
            if sprite_y >= self.offsetY - 32 and sprite_y <= self.screen_height + self.offsetY + 32:
                return True

        return False

    def check_pos(self, player_x):
        """
        Checks Mario's position to determine whether or not the viewport
        camera needs to be shifted
        :param player_location: Two-element tuple representing the x and y
        coordinates
        :return: None
        """
        if player_x > (self.screen_width / 2) + self.offsetX:
            # TODO: Player speed be a passed in parameter soon
            self.offsetX += 6

    def render_ui(self, level):
        '''
        Takes in level information and renders it out
        :param level: This is the level object
        :return: None
        '''
        mario_label = self.myfont.render('SCORE', True, FONT_COLOR)
        coin_label = self.myfont.render('COINS', True, FONT_COLOR)
        world_label = self.myfont.render('WORLD', True, FONT_COLOR)
        time_label = self.myfont.render('TIME', True, FONT_COLOR)
        score = self.myfont.render(str(level.score), True, FONT_COLOR)
        coin = self.myfont.render(str(level.coins), True, FONT_COLOR)
        #level = self.myfont.render('%s - %x' % (test_world_number, test_world_checkpoint), True, FONT_COLOR)
        world_name = self.myfont.render('CS3100', True, FONT_COLOR)
        time = self.myfont.render(str(level.timer), True, FONT_COLOR)

        self.screen.blit(mario_label, (80, 20))
        self.screen.blit(coin_label, (160, 20))
        self.screen.blit(world_label, (240, 20))
        self.screen.blit(time_label, (380, 20))
        self.screen.blit(score, (80, 40))
        self.screen.blit(coin, (160, 40))
        self.screen.blit(world_name, (240, 40))
        self.screen.blit(time, (385, 40))

    def render_sprites(self, player, enemies, blocks, pipes, flags):
        """
        Takes in sprites and locations of the player, enemy, blocks, and pipe
        blocks and renders to the viewport if the sprites are in the viewport
        position.
        :param player_sprite: A pygame image of the main character
        :param player_location: Two-element tuple of x and y coordinates
        :param enemies: List of enemy objects
        :param blocks: List of block objects
        :param pipes: List of pipe objects
        """
        self.check_pos(player.getX_location())

        # Render player sprite
        self.screen.blit(player.image, [player.rect.x - self.offsetX, player.rect.y])

        # Render potential enemies
        if enemies:
            for enemy in enemies:
                if self.in_frame(enemy.rect.x, enemy.rect.y):
                    self.screen.blit(enemy.image, [enemy.rect.x - self.offsetX, enemy.rect.y])
                    enemy.speed = -1

        # Render potential blocks
        if blocks:
            for block in blocks:
                if self.in_frame(block.x, block.rect.y):
                    self.screen.blit(block.image, [block.rect.x - self.offsetX, block.rect.y])
                    #animation += 1
                    #if animation >= 15:
                     #   block_list.update()
                      #  block_list.draw(screen)
                        # pygame.display.flip()
                         #animation = 0

        if flags:
            for flagpole in flags:
                if self.in_frame(flagpole.x, flagpole.y):
                    self.screen.blit(flagpole.image, [flagpole.rect.x - self.offsetX, flagpole.rect.y])
        
        # Render potential pipes
        if pipes:
            for pipe in pipes:
                if self.in_frame(pipe.rect.x, pipe.rect.y):
                    self.screen.blit(pipe.image, [pipe.rect.x - self.offsetX, pipe.rect.y])

    #Renders a death message if the player dies                
    def render_death_message(self, deaths):
        self.screen.fill((0, 0, 0))
        death_message = self.myfont.render('YOU DIED. Lives: ' + str(deaths), True, FONT_COLOR)
        self.screen.blit(death_message, (self.screen_width/2, self.screen_height/2))
    
    #Renders a message if the player wins
    def render_victory_message(self):
        self.screen.fill((0, 0, 0))
        victory_message = self.myfont.render('YOU WON', True, FONT_COLOR)
        self.screen.blit(victory_message, (self.screen_width/2, self.screen_height/2))
