from day_twelve_input import PUZZLE_INPUT, TEST_INPUT
from ship import Ship
from ship_with_waypoint import ShipWithWaypoint


def main():
    HMS_Neil = Ship()
    for instruction in PUZZLE_INPUT.splitlines():
        HMS_Neil.process_instruction(instruction)
    print(HMS_Neil.manhattan_distance)

    Fleet_O_Neil = ShipWithWaypoint()
    for instruction in PUZZLE_INPUT.splitlines():
        Fleet_O_Neil.process_instruction(instruction)
    print(Fleet_O_Neil.ship.manhattan_distance)


if __name__ == "__main__":
    main()
