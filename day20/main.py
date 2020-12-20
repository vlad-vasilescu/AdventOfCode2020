import itertools
import functools
import re

with open('input.txt', 'r') as input_file:
    file = input_file.read().split('\n\n')

tiles = {}
for tile in file:
    tile_id = int(tile.split('\n')[0].strip(':').split(' ')[1])
    tile_img = tile.strip('\n').split('\n')[1:]

    tiles[tile_id] = tile_img

size = int(len(tiles)**0.5)

def get_top_row(tile): return tile[0]
def get_bot_row(tile): return tile[-1]
def get_left_col(tile): return ''.join([line[0] for line in tile])
def get_right_col(tile): return ''.join([line[-1] for line in tile])
def get_edges(tile): return [get_top_row(tile), get_bot_row(tile), get_left_col(tile), get_right_col(tile)]

def rotate_cw(tile): return list(map(''.join, zip(*reversed(tile))))
def flip_vert(tile): return tile[::-1]
def flip_hor(tile): return [line[::-1] for line in tile]

def orientations(tile):
    for i in range(4):
        yield (tile, i, 0)
        yield (flip_hor(tile), i, 1)
        yield (flip_vert(tile), i, 2)

        tile = rotate_cw(tile)

correct_orientation = {}
adj_map = {
    tile_id: {
        (i, j): {'top': (0, 0, 0), 'right': (0, 0, 0), 'down': (0, 0, 0), 'left': (0, 0, 0)} for i, j in itertools.product(range(4), range(3))
    } for tile_id in tiles.keys()
}


for tile_id, tile in tiles.items():
    for orient in orientations(tile):
        for stile_id, stile in tiles.items():
            if stile_id == tile_id: continue

            for sorient in orientations(stile):
                if get_top_row(orient[0]) == get_bot_row(sorient[0]):
                    adj_map[tile_id][(orient[1], orient[2])]['down'] = (stile_id, sorient[1], sorient[2])
                    break
                if get_right_col(orient[0]) == get_left_col(sorient[0]):
                    adj_map[tile_id][(orient[1], orient[2])]['right'] = (stile_id, sorient[1], sorient[2])
                    break
                if get_bot_row(orient[0]) == get_top_row(sorient[0]):
                    adj_map[tile_id][(orient[1], orient[2])]['top'] = (stile_id, sorient[1], sorient[2])
                    break
                if get_left_col(orient[0]) == get_right_col(sorient[0]):
                    adj_map[tile_id][(orient[1], orient[2])]['left'] = (stile_id, sorient[1], sorient[2])
                    break


corners = set()
for tile_id, orient in adj_map.items():
    for orientation, possibilites in orient.items():
        posib_count = 0
        for direction, posib in possibilites.items():
            if posib != (0, 0, 0): posib_count += 1
        if posib_count == 2: corners.add(tile_id)

print(functools.reduce(lambda prod, x: prod * x, corners))


def dfs(tile_id, orient, visited, path, direction=None):
    visited.add(tile_id)
    
    path.append((tile_id, direction, orient))

    for direction, neighbor in adj_map[tile_id][orient].items():
        if neighbor[0] not in visited and neighbor != (0, 0, 0):
            
            dfs(neighbor[0], (neighbor[1], neighbor[2]), visited, path, direction)
    return visited


tile_id = corners.pop()
orientation = (0, 0)

visited = set()
path = []
visited = dfs(tile_id, orientation, visited, path)

index_i = 0
index_j = 0

matrix = [[0 for j in range(size)] for i in range(size)]

for item in path:
    if item[1] == 'top': index_i += 1
    elif item[1] == 'down': index_i -= 1
    elif item[1] == 'left': index_j += 1
    elif item[1] == 'right': index_j -= 1

    matrix[index_i][index_j] = (item[0], *item[2])

matrix = flip_hor(matrix)
# print(*matrix, sep='\n')

for i, line in enumerate(matrix):
    for j, col in enumerate(line):
        tile = tiles[col[0]]
        
        for k in range(col[1]):
            tile = rotate_cw(tile)
        if col[2] == 1: tile = flip_hor(tile)
        elif col[2] == 2: tile = flip_vert(tile)


        tile = tile[1:-1]
        for l, line in enumerate(tile):
            tile[l] = line[1:-1]

        matrix[i][j] = tile

final_tile = ['' for _ in range(len(matrix[0][0]) * size)]
for i, line in enumerate(matrix):
    for j, col in enumerate(line):
        for k, tile_line in enumerate(col): final_tile[i * len(matrix[0][0]) + k] += tile_line

max_dino_count = 0
for i in range(4):
    for j in range(3):
        flip_tile = final_tile.copy()
        if j == 1: flip_tile = flip_hor(final_tile.copy())
        elif j == 2: flip_tile = flip_vert(final_tile.copy())

        dino_count = 0
        for line_id, line in enumerate(flip_tile):
            if line_id >= len(flip_tile) - 2: break
            for char_id, char in enumerate(line):
                if char_id < 18: continue
                if char == '#':
                    second_line = flip_tile[line_id + 1][char_id - 18:char_id + 2]
                    third_line = flip_tile[line_id + 2][char_id - 18:char_id + 2]

                    second_valid = False
                    if second_line[0] == '#' and \
                        second_line[5] == '#' and \
                        second_line[6] == '#' and \
                        second_line[11] == '#' and \
                        second_line[12] == '#' and \
                        second_line[17] == '#' and \
                        second_line[18] == '#' and \
                        second_line[19] == '#': second_valid = True

                    third_valid = False
                    if third_line[1] == '#' and \
                        third_line[4] == '#' and \
                        third_line[7] == '#' and \
                        third_line[10] == '#' and \
                        third_line[13] == '#' and \
                        third_line[16] == '#': third_valid = True

                    if second_valid and third_valid:
                        dino_count += 1

        if dino_count > max_dino_count:
            max_dino_count = dino_count
            best_comb = (i, j)
            best_rot = flip_tile.copy()
    final_tile = rotate_cw(final_tile)

count = 0
for line in final_tile:
    count += line.count('#')

print(count - 15 * max_dino_count)
