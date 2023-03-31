from day_twelve_input import PUZZLE_INPUT
from ship import Ship


def main():
    HMS_Neil = Ship()
    for instruction in PUZZLE_INPUT.splitlines():
        HMS_Neil.process_instruction(instruction)
    print(HMS_Neil.manhattan_distance)


if __name__ == "__main__":
    main()
