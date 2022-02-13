from typing import List
from Bootloader import BootLoader


def read_file(filename: str) -> List[str]:
    """Read file from disk and return list of entries"""
    entries = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            entries.append(line)
    return entries


def main():
    file_entries = read_file("Day8\DayEightInput")
    my_console = BootLoader(file_entries)
    my_console.run_til_loop()
    print(f"Acc = {my_console.accumulator} at start of loop")
    my_console.reset_cpu()
    my_console.run_til_end()
    print(f"Acc = {my_console.accumulator} at end of boot sequence")


if __name__ == "__main__":
    main()
