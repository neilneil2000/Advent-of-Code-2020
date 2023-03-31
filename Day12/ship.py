"""
Representation of a ship for Day 12 Advent of Code 2022
"""
from enum import Enum


class Direction(Enum):
    """Enumeration of Ship position"""

    N = 0
    E = 1
    S = 2
    W = 3
    L = 4
    R = 5
    F = 6


class Ship:
    """Representation of a Ship"""

    direction_degrees = {0: "E", 90: "S", 180: "W", 270: "N"}

    def __init__(self):
        self.north = 0
        self.east = 0
        self.orientation = 0  # degrees clockwise from east

    @property
    def manhattan_distance(self):
        """Return manhattan distance from starting point"""
        return abs(self.north) + abs(self.east)

    def turn(self, degrees: int, clockwise=True):
        """Rotate Ship by degress, in direction indicated by clockwise"""
        if clockwise:
            self.orientation = (self.orientation + degrees) % 360
        else:
            self.orientation = (self.orientation - degrees) % 360

    def process_instruction(self, instruction: str):
        type = Direction[instruction[0]]
        value = int(instruction[1:])
        self.move(value, type)
        pass

    def move(self, distance: int, direction: Direction):
        """Move ship distance in direction"""
        match direction:
            case Direction.N:
                self.north += distance
            case Direction.E:
                self.east += distance
            case Direction.S:
                self.north -= distance
            case Direction.W:
                self.east -= distance
            case Direction.L:
                self.turn(distance, False)
            case Direction.R:
                self.turn(distance, True)
            case Direction.F:
                self.move_forward(distance)

    def move_forward(self, distance: int):
        """Move ship forward based on current orientation"""
        direction = self.direction_degrees[self.orientation]
        self.move(distance, Direction[direction])
