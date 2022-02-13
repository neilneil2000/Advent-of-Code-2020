from typing import List


class DataPort:
    """Representation of data port implementing XMAS protocol"""

    def __init__(self, preamble_length: int) -> None:
        self.preamble_length = preamble_length
        self.history = []

    def assess_new_number(self, number: int) -> bool:
        """Handles new number and returns False if doesn't confirm to XMAS sum protocol"""
        validity = True
        if self.preamble_complete:
            validity = self.is_valid(number)
        self.history.append(number)
        return validity

    def is_valid(self, number: int) -> bool:
        """Returns true if number is a valid sum of two previous digits"""
        for value in self.window:
            remainder = number - value
            if remainder != value and remainder in self.window:
                return True
        return False

    def find_operands(self, target: int) -> List[int]:
        for index in range(len(self.history)):
            operands = self.get_sum_operands(target, index)
            if operands:
                return operands
        return []

    def get_sum_operands(self, target: int, start_index: int) -> List[int]:
        total = 0
        index = start_index
        for index in range(start_index, len(self.history)):
            total += self.history[index]
            if total >= target:
                break
        if total == target:
            return self.history[start_index:index]
        return []

    @property
    def preamble_complete(self):
        if len(self.history) >= self.preamble_length:
            return True
        return False

    @property
    def window(self):
        if len(self.history) < self.preamble_length:
            raise ValueError("Window only valid after preamble is complete")
        return self.history[-self.preamble_length :]
