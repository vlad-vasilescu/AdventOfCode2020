from collections import deque
from copy import deepcopy

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

orig_forest = deque([deque(line.strip()) for line in lines])
combinations = [(-1, -1), (-3, -1), (-5, -1), (-7, -1), (-1, -2)]
prod = 1

for comb in combinations:
    no_trees = 0
    forest = deepcopy(orig_forest)
    for i in range(0, len(forest), -comb[1]):
        for forest_line in forest: forest_line.rotate(comb[0])
        forest.rotate(comb[1])

        if forest[0][0] == '#': no_trees += 1
    prod = prod * no_trees

print(prod)
