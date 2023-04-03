from day_fourteen_input import PUZZLE_INPUT


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


def main():
    my_dock = Dock()
    for instruction in PUZZLE_INPUT.splitlines():
        left, right = instruction.split(" = ")
        if left == "mask":
            my_dock.mask = right
        else:
            address = left[4:-1]
            my_dock.load_memory(int(right), int(address))
    print(my_dock.initialisation_value)


if __name__ == "__main__":
    main()
