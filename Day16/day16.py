from typing import Dict, Set

from day_16_input import NEARBY_TICKETS, RULES, YOUR_TICKET
from ticket_mapper import TicketMapper


def process_rules(rules: Dict[str, str]) -> Dict[str, Set[int]]:
    """Process text based rule input to useable dictionary"""
    processed_rules = {}
    for rule_name, rule_ranges in rules.items():
        rule_ranges = rule_ranges.split(" or ")
        field_values = set()
        for rule_range in rule_ranges:
            start, end = rule_range.split("-")
            field_values = field_values.union(set(range(int(start), int(end) + 1)))
            processed_rules[rule_name] = field_values
    return processed_rules


def process_tickets(tickets: str):
    """Process text based tickets into useable list of tickets"""
    processed_tickets = []
    for ticket in tickets.splitlines():
        ticket = ticket.split(",")
        processed_tickets.append(list(map(int, ticket)))
    return processed_tickets


def main():
    rules = process_rules(RULES)
    valid_values = set().union(*rules.values())
    tickets = process_tickets(NEARBY_TICKETS)

    running_total = 0
    valid_tickets = []

    for ticket in tickets:
        valid_ticket = True
        for entry in ticket:
            if entry not in valid_values:
                running_total += entry
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)

    print(running_total)

    # part2
    my_mapper = TicketMapper(valid_tickets, rules)
    my_mapper.solve_mapping()
    print(my_mapper.mapping)

    my_ticket = YOUR_TICKET.split(",")

    answer = 1
    for name, number in my_mapper.mapping.items():
        if name.startswith("departure"):
            answer *= int(my_ticket[list(number)[0]])
    print(answer)


if __name__ == "__main__":
    main()
