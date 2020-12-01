import itertools

with open('input.txt') as input_file:
    lines = [int(line) for line in input_file.readlines()]

comb2 = [comb for comb in itertools.combinations(lines, 2) if sum(comb) == 2020][0]
print(comb2[0] * comb2[1])

comb3 = [comb for comb in itertools.combinations(lines, 3) if sum(comb) == 2020][0]
print(comb3[0] * comb3[1] * comb3[2])
