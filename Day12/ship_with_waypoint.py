from ship import Ship, Direction


class ShipWithWaypoint:
    def __init__(self):
        self.ship = Ship()
        self.waypoint = Ship(north=1, east=10)

    def process_instruction(self, instruction: str):
        instruction_type = Direction[instruction[0]]
        value = int(instruction[1:])
        match instruction_type:
            case Direction.F:
                for _ in range(value):
                    self.ship.move(self.waypoint.north, Direction.N)
                    self.ship.move(self.waypoint.east, Direction.E)
            case Direction.S | Direction.N | Direction.E | Direction.W:
                self.waypoint.move(value, instruction_type)
            case Direction.L | Direction.R:
                if value not in (90, 180, 270):
                    return
                if value == 180:
                    self.waypoint.north *= -1
                    self.waypoint.east *= -1
                elif (value == 90 and instruction_type == Direction.L) or (
                    value == 270 and instruction_type == Direction.R
                ):
                    new_east = self.waypoint.north * -1
                    self.waypoint.north = self.waypoint.east
                    self.waypoint.east = new_east

                else:
                    north = self.waypoint.east * -1
                    self.waypoint.east = self.waypoint.north
                    self.waypoint.north = north
