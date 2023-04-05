from typing import Tuple


class ConwayCubes:
    def __init__(self, initial_input):
        self.active_cubes = self.__initialise(initial_input)

    def __initialise(self, initial_input):
        cubes = set()
        for x_co_ordinate, row in enumerate(initial_input.splitlines()):
            for y_co_ordinate, cube in enumerate(row):
                if cube == "#":
                    cubes.add((x_co_ordinate, y_co_ordinate, 0))
        return cubes

    def _are_neighbours(
        self, cube_a: Tuple[int, int, int], cube_b: Tuple[int, int, int]
    ) -> bool:
        """Returns True if two cubes are neighours"""
        if cube_a == cube_b:
            return False
        a_x, a_y, a_z = cube_a
        b_x, b_y, b_z = cube_b

        if b_x > a_x + 1:
            return False
        if b_x < a_x - 1:
            return False
        if b_y > a_y + 1:
            return False
        if b_y < a_y - 1:
            return False
        if b_z > a_z + 1:
            return False
        if b_z < a_z - 1:
            return False
        return True

    def _count_active_neighbours(self, focus_cube):
        """Return number of active neighbours a cube has"""
        number_active_neighbours = 0
        for possible_neighbour in self.active_cubes:
            if self._are_neighbours(focus_cube, possible_neighbour):
                number_active_neighbours += 1
        return number_active_neighbours

    def playing_area(self):
        """Returns the size of the playing area given the list of active cubes"""
        x, y, z = zip(*self.active_cubes)
        return min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1, min(z) - 1, max(z) + 1

    def get_next_active_layout(self):
        """Return new cube layout after one round"""
        new_active_cubes = set()
        min_x, max_x, min_y, max_y, min_z, max_z = self.playing_area()
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    next_cube = (x, y, z)
                    active_neighbours = self._count_active_neighbours(next_cube)
                    if active_neighbours == 3:
                        new_active_cubes.add(next_cube)
                        continue
                    if self.is_active(next_cube) and active_neighbours == 2:
                        new_active_cubes.add(next_cube)

        return new_active_cubes

    def is_active(self, cube: Tuple[int, int, int]):
        """Returns True if cube is currently active"""
        return cube in self.active_cubes

    def boot(self):
        """Execute boot sequence"""
        for _ in range(6):
            self.active_cubes = self.get_next_active_layout()

    @property
    def number_of_active_cubes(self):
        return len(self.active_cubes)
