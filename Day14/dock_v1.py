class Dock:
    def __init__(self):
        self.memory = {}
        self.mask = ""

    def apply_mask(self, memory_address: int):
        self.memory[memory_address] &= self.and_mask
        self.memory[memory_address] |= self.or_mask

    def load_memory(self, value, address):
        self.memory[address] = value
        self.apply_mask(address)

    @property
    def and_mask(self):
        return int(self.mask.replace("X", "1"), 2)

    @property
    def or_mask(self):
        return int(self.mask.replace("X", "0"), 2)

    @property
    def initialisation_value(self):
        """Returns sum of all values in memory"""
        total = 0
        for value in self.memory.values():
            total += value
        return total
