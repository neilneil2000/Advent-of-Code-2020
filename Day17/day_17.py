from conway_cubes_4d import ConwayCubes
from day17_input import PUZZLE_INPUT


def main():
    energy_source = ConwayCubes(PUZZLE_INPUT)
    energy_source.boot()
    print(energy_source.number_of_active_cubes)


if __name__ == "__main__":
    main()
