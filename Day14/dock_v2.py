class Dock_v2:
    def __init__(self):
        self.memory = {}
        self.mask = ""

    def load_memory(self, value, base_address):
        for address in self.compute_addresses(base_address):
            self.memory[address] = value

    def compute_addresses(self, base_address):
        base_address |= self.zero_mask
        base_address &= self.two_mask
        addresses = []
        floaters = [
            position for position, bit in enumerate(self.mask[::-1]) if bit == "X"
        ]
        for i in range(2 ** len(floaters)):
            total = 0
            format_string = f"0{len(floaters)}b"
            for a, b in zip(format(i, format_string), floaters):
                total += int(a) * 2**b
            addresses.append(base_address + total)

        return addresses

    @property
    def zero_mask(self):
        return int(self.mask.replace("X", "0"), 2)

    @property
    def two_mask(self):
        temp_mask = self.mask.replace("0", "1")
        return int(temp_mask.replace("X", "0"), 2)

    @property
    def initialisation_value(self):
        """Returns sum of all values in memory"""
        total = 0
        for value in self.memory.values():
            total += value
        return total
