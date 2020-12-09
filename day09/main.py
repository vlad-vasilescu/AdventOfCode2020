from itertools import combinations
from itertools import accumulate

with open('input.txt', 'r') as input_file:
    lines = [int(line.strip()) for line in input_file.readlines()]

preamble = 25
for i in range(preamble, len(lines)):
    previous_combs = combinations(lines[i - preamble:i], 2)
    has_valid_preamble = False
    for comb in previous_combs:
        if comb[0] + comb[1] == lines[i]: has_valid_preamble = True

    if not has_valid_preamble:
        invalid_num = lines[i]
        break

print(invalid_num)

def get_contiguous_sets(iterable):
    for i, j in combinations(range(len(iterable)), 2):
        yield iterable[i:j]


for subset in get_contiguous_sets(lines):
    if sum(subset) == invalid_num:
        print(min(subset) + max(subset))
        break
