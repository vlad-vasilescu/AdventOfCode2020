from copy import deepcopy


with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

instr_set = []
visited = {}
index = 0
for line in lines:
    instr = line.split(' ')[0]
    arg = int(line.split(' ')[1])

    instr_set.append([instr, arg])
    visited[index] = 0
    index += 1


def debug_program(instr_set):
    visited = {}
    for index in range(0, len(instr_set)): visited[index] = 0

    accumulator = 0
    index = 0
    while True:
        if index >= len(instr_set): return ('normal', accumulator)
        if visited[index] == 1: return ('loop', accumulator)
        visited[index] += 1

        instr = instr_set[index][0]
        arg = instr_set[index][1]

        if instr == 'nop':
            index += 1
        elif instr == 'acc':
            accumulator += arg
            index += 1
        elif instr == 'jmp':
            index += arg

print(debug_program(instr_set)[1])

for i in range(0, len(instr_set)):
    new_set = deepcopy(instr_set)

    if instr_set[i][0] == 'nop':
        new_set[i][0] = 'jmp'
    elif instr_set[i][0] == 'jmp':
        new_set[i][0] = 'nop'
    
    output = debug_program(new_set)
    if output[0] == 'normal': print(output[1])
