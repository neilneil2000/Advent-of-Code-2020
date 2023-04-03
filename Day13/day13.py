from typing import List, Tuple

from day_thirteen_input import (
    PUZZLE_BUSES,
    PUZZLE_TIMESTAMP,
    TEST_TIMESTAMP,
    TEST_BUSES,
)


def modular_inverse(Mi: int, mod: int):
    """
    Returns Modular inverse Z of M
    MZ = remainder % mod
    """
    attempt = -1
    Zi = 0
    while attempt != 1:
        Zi += 1
        attempt = (Zi * Mi) % mod

    return Zi


def chinese_remainder_theorem(congruences: List[Tuple]) -> int:
    """
    An implementatino of the Chinese Remainder Theorem to solve a list of modular congruences.
    each list entry should consist of a tuple (a,n) representing x=a mod n
    """
    equations = {mod: remainder for (remainder, mod) in congruences}
    total = 0

    M = 1
    for mod_i in equations.keys():
        M *= mod_i

    for mod_i in equations.keys():
        Mi = int(M / mod_i)
        Zi = modular_inverse(Mi, mod_i)
        total += equations[mod_i] * Mi * Zi

    return total % M


def part_2_clunky(buses: list):
    bus_gaps = {}
    for gap, bus in enumerate(buses):
        if bus == "x":
            continue
        bus_gaps[int(bus)] = gap
    print(bus_gaps)
    timestamp = 0 - bus_gaps[647]
    flag = True
    last_print = 0
    while flag:
        flag = False
        timestamp += 647
        if timestamp > last_print + 1_000_000_000:
            print(".", end="")
            last_print = timestamp
        for bus, gap in bus_gaps.items():
            if (timestamp + gap) % bus != 0:
                flag = True
                break
    print(timestamp)


def main():
    buses = PUZZLE_BUSES.split(",")
    wait_times = {}
    for bus in buses:
        if bus == "x":
            continue
        wait_times[int(bus)] = int(bus) - PUZZLE_TIMESTAMP % int(bus)
    best_bus = min(wait_times, key=wait_times.get)
    print(best_bus * wait_times[best_bus])

    # part2
    buses = [
        (int(bus_number) - position, int(bus_number))
        for position, bus_number in enumerate(buses)
        if bus_number != "x"
    ]
    print(chinese_remainder_theorem(buses))


if __name__ == "__main__":
    main()
