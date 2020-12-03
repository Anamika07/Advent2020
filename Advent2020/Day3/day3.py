def input_data():
    with open("day3_input.txt", 'r') as input_file:
        rows = []
        for lines in input_file:
            rows.append(lines.replace('\n', ''))
    return rows


def is_tree(coordinates, map_):
    col_l = len(map_[coordinates[0]])
    coordinates_of = map_[coordinates[0]][coordinates[1] % col_l]
    return coordinates_of == '#'


def count_trees(move, coordinates, map_):
    trees = 0
    rows = len(map_) - 1
    while coordinates[0] < rows:
        coordinates = (coordinates[0] + move[0], coordinates[1] + move[1])
        if is_tree(coordinates, map_):
            trees = trees + 1
    return trees


def puzzle1(move=(1, 3)):
    map_grid = input_data()
    coordinates = (0, 0)
    return count_trees(move, coordinates, map_grid)


def puzzle2():
    moves = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    tree_count_product = 1
    for move in moves:
        tree_count = puzzle1(move)
        tree_count_product = tree_count_product * tree_count
    return tree_count_product


print(f"Solution for Puzzle 1: {puzzle1()}")
print(f"Solution for Puzzle 2: {puzzle2()}")
