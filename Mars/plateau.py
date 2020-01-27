class Plateau(object):
    MINIMUM_WIDTH = 0
    MINIMUM_HEIGHT = 0

    def __init__(self, width, height, minimum_width=0, minimum_height=0):
        self.width = width
        self.height = height
        self.MIN_WIDTH = minimum_width
        self.MIN_HEIGHT = minimum_height

    def space_available(self, position):
        """
        :param Position position:
        :return:
        """
        return self.MINIMUM_WIDTH <= position.x <= self.width and self.MINIMUM_HEIGHT <= position.y <= self.height
