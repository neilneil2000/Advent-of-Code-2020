from typing import List

from Adapters import Adapters


def read_file(filename: str) -> List[int]:
    number_list = []
    with open(filename, "r") as f:
        for line in f:
            number_list.append(int(line.strip()))
    return number_list


def main():
    adapter_list = read_file("Day10\DayTenInput")
    my_adapters = Adapters()
    my_adapters.populate_new_adapters(adapter_list)
    one = my_adapters.one_jolt_gaps
    three = my_adapters.three_jolt_gaps
    answer = one * three
    print(f"Part 1 Answer is: {answer} ({one} x {three})")
    my_adapters.count_combos()
    print(f"Total Combos: {my_adapters.total_combos}")


if __name__ == "__main__":
    main()
