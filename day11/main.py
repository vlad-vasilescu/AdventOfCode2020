from copy import deepcopy

with open('input.txt', 'r') as input_file:
    lines = [list(line.strip()) for line in input_file.readlines()]

adjancent = [-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j]

def get_adj_of(location, seat):
    count = 0
    for adj in adjancent:
        src = location + adj
        if src.real < 0 or src.real >= len(lines): continue
        if src.imag < 0 or src.imag >= len(lines[0]): continue

        if lines[int(src.real)][int(src.imag)] == seat: count += 1
    return count

def get_in_line(location, seat):
    count = 0
    for adj in adjancent:
        src = location + adj
        while src.real >= 0 and src.real < len(lines) and src.imag >= 0 and src.imag < len(lines[0]):
            if lines[int(src.real)][int(src.imag)] == '.':
                src += adj
            elif lines[int(src.real)][int(src.imag)] == seat:
                count += 1
                break
            else: break
    return count

while True:
    changed = 0
    new_lines = deepcopy(lines)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'L':
                # if get_adj_of(complex(i, j), '#') == 0:
                if get_in_line(complex(i, j), '#') == 0:
                    new_lines[i][j] = '#'
                    changed += 1
            if lines[i][j] == '#':
                # if get_adj_of(complex(i, j), '#') >= 4:
                if get_in_line(complex(i, j), '#') >= 5:
                    new_lines[i][j] = 'L'
                    changed += 1
    
    lines = new_lines
    if changed == 0: break

count = 0
for line in lines:
    count += line.count('#')
print(count)

