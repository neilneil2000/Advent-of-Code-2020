from typing import List

from BagRules import BagRules


def read_file(filename: str) -> List[str]:
    """Read file from disk and return list of entries"""
    entries = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            entries.append(line)
    return entries


def main():
    file_entries = read_file("Day7\DaySevenInput")
    my_rules = BagRules(file_entries)
    my_rules.initialise()

    bag_type = "shiny gold"

    valid_outer_bags = my_rules.indirect_container(bag_type)
    print(f"{len(valid_outer_bags)} bags can contain a {bag_type} bag")

    how_many = my_rules.how_many_inside(bag_type)
    print(f"{how_many} bags inside one {bag_type} bag")


if __name__ == "__main__":
    main()
