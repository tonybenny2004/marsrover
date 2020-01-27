from .position import Position


class Rovers(object):
    available_commands = {
        'M': 'move',
        'L': 'left_turn',
        'R': 'right_turn',
    }
    directions = {'N': 1, 'E': 2, 'S': 3, 'W': 4}
    heading = directions['N']

    def __init__(self, plateau, position, heading):
        """
        Initializing Rovers  With Below Params
        :param plateau:
        :param position:
        :param heading:
        """
        self.plateau = plateau
        self.position = position
        self.heading = heading

    @property
    def __str__(self):
        return self.current_position

    def set_position(self, x, y, heading):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position.x = x
            self.position.y = y

        self.heading = heading

    def current_position(self):
        return '{0} {1} {2}'.format(self.position.x, self.position.y, self.get_heading)

    @property
    def get_heading(self):
        directions = list(self.directions.keys())

        try:
            direction = directions[self.heading - 1]
        except IndexError:
            direction = 'N'
            print('Direction error...')

        return direction

    def validate_instruction(self, instructions):
        if instructions.find('LM') || instructions.find('LMR') != -1:
            self.process_instruction(instructions)
        else:
            print("Wrong Instruction String")
            exit()

    def process_instruction(self, commands):

        for i in range(len(commands)):
            self.run_instruction(commands[i])

    def run_instruction(self, command):

        if 'L' == command:
            self.left_turn()
        elif 'R' == command:
            self.right_turn()
        elif 'M' == command:
            if not self.move_rover():
                print("You are trying to go to wrong Place")

    def move_rover(self):
        if not self.plateau.space_available(self.position):
            return False
        # Assume that the square directly North from (x, y) is (x, y+1).
        if self.directions['N'] == self.heading:
            self.position.y += 1
        elif self.directions['E'] == self.heading:
            self.position.x += 1
        elif self.directions['S'] == self.heading:
            self.position.y -= 1
        elif self.directions['W'] == self.heading:
            self.position.x -= 1

        return True

    def left_turn(self):
        self.heading = self.directions['W'] if (self.heading - 1) < self.directions['N'] else self.heading - 1

    def right_turn(self):
        self.heading = self.directions['N'] if (self.heading + 1) > self.directions['W'] else self.heading + 1
