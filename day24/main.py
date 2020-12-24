with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

locations = set()
buffer = ''
for line in lines:
    pos = (0, 0, 0)
    for char in line:
        if char == 'e':
            if len(buffer):
                if buffer + char == 'ne': pos = (pos[0] + 1, pos[1], pos[2] - 1)
                if buffer + char == 'se': pos = (pos[0], pos[1] - 1, pos[2] + 1)
            else: pos = (pos[0] + 1, pos[1] - 1, pos[2])
            buffer = ''
        if char == 'w':
            if len(buffer):
                if buffer + char == 'nw': pos = (pos[0], pos[1] + 1, pos[2] - 1)
                if buffer + char == 'sw': pos = (pos[0] - 1, pos[1], pos[2] + 1)
            else: pos = (pos[0] - 1, pos[1] + 1, pos[2])
            buffer = ''
        if char == 's' or char == 'n': buffer += char
    if pos in locations: locations.remove(pos)
    else: locations.add(pos)

print(len(locations))

def get_adj(tile):
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x + y + z == 0 and (tile[0] + x, tile[1] + y, tile[2] + z) != tile:
                    yield (tile[0] + x, tile[1] + y, tile[2] + z)


grid = locations
for _ in range(100):
    new_grid = grid.copy()
    for tile in grid:

        adj_black = 0
        for adj in get_adj(tile):
            if adj in grid: adj_black += 1
        if adj_black == 0 or adj_black > 2: new_grid.remove(tile)

    for tile in grid:
        for adj in get_adj(tile):
            if adj in grid: continue

            adj_adj_black = 0
            for adj_adj in get_adj(adj):
                if adj_adj in grid: adj_adj_black += 1
            if adj_adj_black == 2: new_grid.add(adj)

    grid = new_grid

print(len(grid))
