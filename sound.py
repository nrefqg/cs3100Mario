import pygame

class SoundClass:
    """
    Class that stores instances of sounds so we don't have to recreate
    these instances and waste memory
    """
    def __init__(self):
        """
        Initializes all audio files.
        :return: None
        """
        # Initialize sound effect channel
        self.channel = pygame.mixer.Channel(0)
        self.channel.set_volume(0.5)
        # Load audio files
        self.jump = pygame.mixer.Sound('sounds/jump.ogg')
        self.jump.set_volume(0.15)
        self.death = pygame.mixer.Sound('sounds/death.ogg')
        self.victory = pygame.mixer.Sound('sounds/victory.wav')
        self.block_hit = pygame.mixer.Sound('sounds/block_hit.wav')
        self.block_hit.set_volume(1.5)
        self.coin = pygame.mixer.Sound('sounds/coin.wav')
        self.powerup = pygame.mixer.Sound('sounds/power_up.wav')
    
    def start_bg(self):
        """
        Starts background music.
        :return: None
        """
        pygame.mixer.music.load('sounds/background.ogg')
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1)

    def stop_bg(self):
        """
        Stops background music.
        :return: None
        """
        pygame.mixer.music.stop()

    def play_sound(self, sound):
        """
        Plays sound effect based upon passed in parameters
        :sound: A string specifyng what sound to play
        :return: None
        """
        if sound == "jump":
            self.channel.play(self.jump)
        elif sound == "death":
            self.channel.play(self.death)
        elif sound == "victory":
            self.channel.play(self.victory)
        elif sound == "block_hit":
            self.channel.play(self.block_hit)
        elif sound == "coin":
            self.channel.play(self.coin)
        elif sound == "powerup":
            self.channel.play(self.powerup)

