TEST_INPUT = [3, 1, 2]
PUZZLE_INPUT = [6, 4, 12, 1, 20, 0, 16]


def main():
    starting_numbers = PUZZLE_INPUT
    number_of_rounds = 30_000_000
    game = {
        number: position + 1
        for position, number in enumerate(starting_numbers)
        if position < len(starting_numbers) - 1
    }
    say_next = starting_numbers[-1]
    for turn in range(len(starting_numbers), number_of_rounds + 1):
        if game.get(say_next) is None:
            game[say_next] = turn
            say_next = 0
            continue
        say_next_temp = turn - game[say_next]
        game[say_next] = turn
        say_next = say_next_temp
    for key, value in game.items():
        if value == number_of_rounds:
            print(key)


if __name__ == "__main__":
    main()
