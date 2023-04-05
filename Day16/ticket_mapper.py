from typing import List, Set, Dict


class TicketMapper:
    """Class that maps tickets to fields"""

    def __init__(self, tickets: List[List], rules: Dict[str, Set]):
        self.tickets = tickets
        self.rules = rules
        self.mapping = None

    def initialise_mapping(self):
        """Create a mapping table of field_names to possible ticket_fields"""
        mapping = {field_name: set() for field_name in self.rules}
        for field_name, field_possibilities in self.rules.items():
            for field_number, field_values in enumerate(self.tickets_by_field):
                if set(field_values).issubset(field_possibilities):
                    mapping[field_name].add(field_number)
        return mapping

    def solve_mapping(self):
        """Figure out which fields map where"""
        self.mapping = self.initialise_mapping()
        while any(len(possibilities) > 1 for possibilities in self.mapping.values()):
            for field_possibilities in self.mapping.values():
                if len(field_possibilities) == 1:
                    self.remove_references_to(list(field_possibilities)[0])

    def remove_references_to(self, group):
        """Remove all references to group within field_mapping except where it is the only value in the group"""
        for field_possibles in self.mapping.values():
            if len(field_possibles) == 1:
                continue
            field_possibles.discard(group)

    @property
    def tickets_by_field(self):
        """Transposes Tickets to return them grouped by field"""
        return zip(*self.tickets)
