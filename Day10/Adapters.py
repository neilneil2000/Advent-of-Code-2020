class Adapters:
    def __init__(self) -> None:
        self.adapter_list = [0]
        self.adapter_tree = {}
        self.reverse_tree = {}
        self.paths_from = {}

    def populate_new_adapters(self, adapter_list):
        self.adapter_list.extend(adapter_list)
        self.add_device_joltage()
        self.sort_adapters()

    def sort_adapters(self):
        self.adapter_list.sort()

    def add_device_joltage(self):
        self.adapter_list.append(max(self.adapter_list) + 3)

    def create_tree(self):
        for adapter in self.adapter_list:
            self.adapter_tree[adapter] = []
            for other_adapter in self.adapter_list:
                if 1 <= other_adapter - adapter <= 3:
                    self.adapter_tree[adapter].append(other_adapter)

    def create_reverse_tree(self):
        for adapter in self.adapter_list:
            self.reverse_tree[adapter] = []
            for other_adapter in self.adapter_list:
                if 1 <= adapter - other_adapter <= 3:
                    self.reverse_tree[adapter].append(other_adapter)

    def count_combos(self):
        if not self.adapter_tree:
            self.create_tree()
            self.create_reverse_tree()
            self.paths_from[0] = 1
        for key, valid_adpaters in self.reverse_tree.items():
            if key > 0:
                total_paths = 0
                for adapter in valid_adpaters:
                    total_paths += self.paths_from[adapter]
                self.paths_from[key] = total_paths

    def _jolt_gap(self, gap_size: int):
        counter = 0
        for index in range(1, len(self.adapter_list)):
            if self.adapter_list[index] - self.adapter_list[index - 1] == gap_size:
                counter += 1
        return counter

    @property
    def total_combos(self):
        return self.paths_from[self.adapter_list[-1]]

    @property
    def one_jolt_gaps(self):
        return self._jolt_gap(gap_size=1)

    @property
    def three_jolt_gaps(self):
        return self._jolt_gap(gap_size=3)
