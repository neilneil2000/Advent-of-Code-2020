from waiting_area import WaitingArea


def read_file(filename: str) -> list:
    grid = []
    with open(filename, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    return grid


def main():
    waiting_room_layout = read_file("Day11/DayElevenInput")
    airport = WaitingArea(waiting_room_layout)
    print("STARTING LAYOUT")
    airport.print_seating()
    steps = 0
    while airport.last_step_changes != 0:
        steps += 1
        airport.execute_step()
    print()
    print(f"AFTER STEP {steps-1}")
    airport.print_seating()

    print(f"STABLE AFTER {steps-1} steps")
    print(f"{airport.occupied_seats} seats occupied")


if __name__ == "__main__":
    main()
