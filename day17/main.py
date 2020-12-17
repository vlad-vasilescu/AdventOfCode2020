with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

active = set()
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#': active.add((j, i, 0, 0))


def get_adj(point):
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for k in range(-1, 2):
                    yield (point[0] + x, point[1] + y, point[2] + z, point[3] + k)


for i in range(6):
    print(i)
    new_state = active.copy()
    for point in active:
        point_adj_act = 0
        for adj in get_adj(point):
            if adj == point: continue
            if adj in active: point_adj_act += 1
            else:
                adj_adj_act = 0

                for adj_adj in get_adj(adj):
                    if adj_adj in active: adj_adj_act += 1

                if adj_adj_act == 3: new_state.add(adj)
        
        if point_adj_act == 2 or point_adj_act == 3: continue
        else: new_state.remove(point)
    active = new_state

print(len(active))
