from multiprocessing.connection import wait
from waiting_area import WaitingArea


def read_file(filename: str) -> list:
    grid = []
    with open(filename, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    return grid


def main():
    waiting_room_layout = read_file("Day11\DayElevenInput")
    Airport = WaitingArea(waiting_room_layout)
    print("STARTING LAYOUT")
    Airport.print_seating()
    x = 0
    while Airport.last_step_changes != 0:
        x += 1
        Airport.execute_step()
    print()
    print(f"AFTER STEP {x-1}")
    Airport.print_seating()

    print(f"STABLE AFTER {x-1} steps")
    print(f"{Airport.count_occupied_seats()} seats occupied")


if __name__ == "__main__":
    main()
