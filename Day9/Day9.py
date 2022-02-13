from typing import List

from DataPort import DataPort


def readfile(filename: str) -> List[int]:
    input_numbers = []
    with open(filename, "r") as f:
        for line in f:
            input_numbers.append(int(line.strip()))
    return input_numbers


def main():
    input_values = readfile("Day9\DayNineInput")
    AeroplanePort = DataPort(preamble_length=25)
    for number in input_values:
        if not AeroplanePort.assess_new_number(number):
            print(f"Value {number} is not valid")
            break
    operands = AeroplanePort.find_operands(number)
    weakness = min(operands) + max(operands)
    print(f"Encrption Weakness is {weakness}")


if __name__ == "__main__":
    main()
