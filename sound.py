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
        # Load audio files
    
    def start_bg(self):
        pygame.mixer.music.load('sounds/background.ogg')
        pygame.mixer.music.play(-1)

    def stop_bg(self):
        pygame.mixer.music.stop()
