from day_thirteen_input import (
    PUZZLE_BUSSES,
    PUZZLE_TIMESTAMP,
    TEST_TIMESTAMP,
    TEST_BUSSES,
)


def main():
    buses = PUZZLE_BUSSES.split(",")
    wait_times = {}
    for bus in buses:
        if bus == "x":
            continue
        wait_times[int(bus)] = int(bus) - PUZZLE_TIMESTAMP % int(bus)
    best_bus = min(wait_times, key=wait_times.get)
    print(best_bus * wait_times[best_bus])


if __name__ == "__main__":
    main()
