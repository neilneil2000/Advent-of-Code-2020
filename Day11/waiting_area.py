from typing import Tuple


class WaitingArea:

    EMPTY_SEAT = "L"
    OCCUPIED_SEAT = "#"
    FLOOR = "."

    def __init__(self, seats: list):
        self.seating = seats
        self.rows = len(self.seating)
        self.columns = len(self.seating[0])
        self.last_step_changes = None

    def print_seating(self):
        for row in self.seating:
            for space in row:
                print(space, end="")
            print()

    def count_occupied_seats(self)-> int:
        occupied_seats = 0
        for row in self.seating:
            for space in row:
                if space == self.OCCUPIED_SEAT:
                    occupied_seats += 1
        return occupied_seats

    def adjacent_occupants(self, seat_location: Tuple[int, int]) -> int:
        """Check whether seats nearby are occupied and returns total of occupied seats"""
        row, column = seat_location
        possible_adjacencies = {
            (row - 1, column - 1),
            (row - 1, column),
            (row - 1, column + 1),
            (row, column - 1),
            (row, column + 1),
            (row + 1, column - 1),
            (row + 1, column),
            (row + 1, column + 1),
        }
        adjacencies = set()
        for space in possible_adjacencies:
            row, column = space
            if (
                0 <= row < self.rows
                and 0 <= column < self.columns
                and self.seating[row][column] == self.OCCUPIED_SEAT
            ):
                adjacencies.add(space)
        return len(adjacencies)

    def set_change_count(self, new_seating: list):
        changes = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.seating[row][column] != new_seating[row][column]:
                    changes += 1
        self.last_step_changes = changes

    def execute_step(self):
        new_seating = []
        for row in range(self.rows):
            new_row = []
            for column in range(self.columns):
                space = self.seating[row][column]
                if space == self.FLOOR:
                    new_row.append(self.FLOOR)
                elif space == self.EMPTY_SEAT:
                    if self.adjacent_occupants((row, column)) == 0:
                        new_row.append(self.OCCUPIED_SEAT)
                    else:
                        new_row.append(self.EMPTY_SEAT)
                elif space == self.OCCUPIED_SEAT:
                    if self.adjacent_occupants((row, column)) >= 4:
                        new_row.append(self.EMPTY_SEAT)
                    else:
                        new_row.append(self.OCCUPIED_SEAT)
            new_seating.append(new_row)
        self.set_change_count(new_seating)
        self.seating = new_seating
