from typing import List, Set


class BagRules:
    """Class respresenting and executing rules"""

    def __init__(self, entries: List[str]):
        self.entries = entries
        self.rules = {}

    def initialise(self):
        self._process_entries()

    def _process_entries(self):
        """Create Ruleset from natural language entries"""
        for entry in self.entries:
            self._process_entry(entry)

    def _process_entry(self, entry: str):
        """Process individual entry"""
        container, allowed = entry.split("contain")
        container = container[: container.find(" bag")]
        self.rules[container] = []  # Assume no duplicates in entry list
        if allowed.find("no other bags") != -1:
            return

        allowed = allowed.strip().split(",")

        for bag in allowed:
            number, bag_type = bag.strip().split(" ", 1)
            bag_type = bag_type[: bag_type.find(" bag")]
            self.rules[container].append((int(number), bag_type))

    def could_contain(self, outer: str, inner: str) -> bool:
        """Return True is inner could be in outer"""
        if outer not in self.rules.keys():
            return False
        for _, bag_type in self.rules[outer]:
            if inner == bag_type:
                return True
        for _, interim in self.rules[outer]:
            if self.could_contain(interim, inner):
                return True
        return False

    def indirect_container(self, target_bag_type: str) -> Set[str]:
        """Return bags that can contain a bag of 'bag_type' directly or indirectly"""
        valid_outer_bags = set()
        for bag_type in self.rules:
            if bag_type != target_bag_type:  # Don't bother looking in same bag type
                if self.could_contain(bag_type, target_bag_type):
                    valid_outer_bags.add(bag_type)
        return valid_outer_bags

    def how_many_inside(self, outer_bag_type: str) -> int:
        """Returns number of bags inside a bag of bag_type, or -1 on error"""
        if outer_bag_type not in self.rules.keys():
            return -1

        if not self.rules[outer_bag_type]:
            return 0

        total_inside = 0
        for number, inner_bag_type in self.rules[outer_bag_type]:
            total_inside += number * (self.how_many_inside(inner_bag_type) + 1)

        return total_inside
