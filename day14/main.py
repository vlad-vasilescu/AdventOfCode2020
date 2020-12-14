import itertools

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

memory = {}
for line in lines:
    line = line.split(' = ')
    if line[0] == 'mask': mask = line[1]
    else:
        addr = int(line[0].split('[')[1].strip(']'))
        value = "{0:b}".format(int(line[1])).zfill(36)
        
        value = list(value)
        for i in range(0, 36):
            if mask[i] != 'X': value[i] = mask[i]

        value = ''.join(value)
        memory[addr] = value

mem_sum = 0
for mem in memory.values(): mem_sum += int(mem, 2)
print(mem_sum)

memory = {}
for line in lines:
    line = line.split(' = ')
    if line[0] == 'mask': mask = line[1]
    else:
        addr = int(line[0].split('[')[1].strip(']'))
        addr = list("{0:b}".format(addr).zfill(36))
        value = "{0:b}".format(int(line[1])).zfill(36)

        for i in range(0, 36):
            if mask[i] != '0': addr[i] = mask[i]

        unkn = addr.count('X')
        combs = [list(comb) for comb in itertools.product(['0', '1'], repeat=unkn)]
        for comb in combs:
            new_addr = addr.copy()
            
            for i in range(0, 36):
                if new_addr[i] == 'X':
                    new_addr[i] = comb[0]
                    comb.pop(0)

            memory[int(''.join(new_addr))] = value

mem_sum = 0
for mem in memory.values(): mem_sum += int(mem, 2)
print(mem_sum)
