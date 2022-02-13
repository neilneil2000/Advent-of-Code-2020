class DataPort:
    """Representation of data port implementing XMAS protocol"""

    def __init__(self, preamble_length: int) -> None:
        self.preamble_length = preamble_length
        self.window = []

    def assess_new_number(self, number: int) -> bool:
        """Handles new number and returns False if doesn't confirm to XMAS sum protocol"""
        if len(self.window) == self.preamble_length:
            validity = self.is_valid(number)
            self.window.append(number)
            self.window.pop(0)
            return validity
        self.window.append(number)
        return True

    def update_history(self, number: int) -> None:
        """Update log of previously received numbers"""
        self.window.append(number)

    def is_valid(self, number: int) -> bool:
        """Returns true if number is a valid sum of two previous digits"""
        for value in self.window:
            remainder = number - value
            if remainder != value and remainder in self.window:
                return True
        return False
