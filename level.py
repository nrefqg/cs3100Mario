
class Level:
    """Class for storing information about the progression through a level"""

    def __init__(self, layout, time):
        """
        Constructor for a level
        :param layout: The list of sprites and objects in the level
        :param time: The allotted to complete the level in seconds
        """

        if time is not int:
            raise ValueError("Argument time should be an integer")
        elif time <= 0:
            raise ValueError("Argument time should be greater than 0")

        self.layout = layout
        self.time = time
        self.timer = time
        self.score = 0
        self.coins = 0
        self.checkpoint = None

    def tick(self):
        """
        Tick down the timer
        :return: False to signal that the timer has reached 0, True otherwise
        """
        if self.timer == 0:
            return False
        self.timer -= 1
        return True

    def reset(self):
        """
        Resets certain parts of the level (e.g. upon dying and respawning)
        :return: None
        """
        self.timer = self.time
        self.score = 0
        self.coins = 0
