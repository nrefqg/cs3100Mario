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
        # Load audio files
        self.jump = pygame.mixer.Sound('sounds/jump.ogg')
        self.jump.set_volume(0.25)
        self.death = pygame.mixer.Sound('sounds/death.ogg')
        self.victory = pygame.mixer.Sound('sounds/victory.ogg')

    
    def start_bg(self):
        """
        Starts background music.
        :return: None
        """
        pygame.mixer.music.load('sounds/background.ogg')
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

