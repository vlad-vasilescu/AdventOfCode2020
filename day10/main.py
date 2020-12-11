import itertools
import functools

with open('input.txt', 'r') as input_file:
    lines = [int(line.strip()) for line in input_file.readlines()]

lines = sorted(lines)

prev_jolt = 0
count_one = 0
count_three = 0

for line in lines:
    if line - prev_jolt == 1: count_one += 1
    elif line - prev_jolt == 3: count_three += 1

    prev_jolt = line
prev_jolt += 3
count_three += 1
print(count_one * count_three)

device = max(lines)

@functools.lru_cache(None)
def get_arrangement_no(start):
    if start == device: return 1
    
    count = 0
    for i in range(1, 4):
        if start + i not in lines: continue
        count += get_arrangement_no(start + i)
    
    return count

print(get_arrangement_no(0))
