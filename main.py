from Mars import Plateau
from Mars import Position
from Mars import Rovers





def main():
    plateau = Plateau(5, 5)
    position = Position(1, 2)
    # Create rover instance
    rovers = Rovers(plateau, position, Rovers.directions.get('N'))
    instructions = input('Enter NASA Instructions:')

    rovers.validate_instruction(instructions)
    print(rovers)  # prints 1 3 N
    rovers.set_position(3, 3, Rovers.directions.get('E'))
    instructions_new = input('Enter NASA New Instructions:')
    rovers.validate_instruction(instructions_new)
    print(rovers)  # prints 5 1 E


if __name__ == "__main__":
    main()
