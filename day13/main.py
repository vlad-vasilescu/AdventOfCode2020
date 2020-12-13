import math

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

first_depart = int(lines[0])
departs = {}
for bus in lines[1].split(','):
    if bus == 'x': continue
    bus = int(bus)
    next_depart = (math.floor(first_depart / bus) + 1) * bus
    departs[next_depart] = bus

print(departs[min(departs.keys())] * (min(departs.keys()) - first_depart))


busses = lines[1].split(',')
for bus in busses:
    # copy and paste this into wolfram alpha for solution
    if bus != 'x': print(f"(t + {busses.index(bus)}) mod {bus} = 0;")
