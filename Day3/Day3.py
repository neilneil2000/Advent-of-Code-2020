from map import Map

def main():
    slopes = []
    directions = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for index,direction in enumerate(directions):
        slopes.append(Map("Day3/DayThreeInput"))
        slopes[index].mark_descent(direction)
        slopes[index].count_trees()
        print(f'{slopes[index].trees_hit} trees hit')

    trees_hit = 1
    for slope in slopes:
        trees_hit *= slope.trees_hit
    print(f'Answer: {trees_hit}')


if __name__ == "__main__":
    main()