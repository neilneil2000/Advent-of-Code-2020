from day_fourteen_input import PUZZLE_INPUT, TEST_INPUT


from dock_v1 import Dock
from dock_v2 import Dock_v2


def main():
    my_dock = Dock()
    my_dock_v2 = Dock_v2()
    for instruction in PUZZLE_INPUT.splitlines():
        left, right = instruction.split(" = ")
        if left == "mask":
            my_dock.mask = right
            my_dock_v2.mask = right
        else:
            address = left[4:-1]
            my_dock.load_memory(int(right), int(address))
            my_dock_v2.load_memory(int(right), int(address))

    print(my_dock.initialisation_value)
    print(my_dock_v2.initialisation_value)


if __name__ == "__main__":
    main()
