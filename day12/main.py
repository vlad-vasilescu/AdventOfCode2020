with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

directions = {'N': 1, 'S': -1, 'E': -1j, 'W': 1j}
face_left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
face_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

facing = 'E'
loc = 0

for line in lines:
    action = line[0]
    length = int(line[1:])
    
    if action == 'F':
        loc += length * directions[facing]
    elif action == 'L':
        for i in range(length // 90):
            facing = face_left[facing]
    elif action == 'R':
        for i in range(length // 90):
            facing = face_right[facing]
    else:
        loc += length * directions[action]

print(int(abs(loc.real) + abs(loc.imag)))

loc = 0
waypoint = 1-10j

def rotate_waypoint(direction):
    global waypoint
    if direction == 'R': sine = 1
    elif direction == 'L': sine = -1

    waypoint -= loc
    
    imag_part = - (waypoint.real * sine)
    real_part = waypoint.imag * sine
    waypoint = real_part + imag_part * 1j
    
    waypoint += loc

for line in lines:
    action = line[0]
    length = int(line[1:])

    if action == 'F':
        delta = waypoint - loc
        loc += length * delta
        waypoint += length * delta
    elif action == 'L':
        for i in range(length // 90):
            rotate_waypoint(action)
    elif action == 'R':
        for i in range(length // 90):
            rotate_waypoint(action)
    else:
        waypoint += length * directions[action]

print(int(abs(loc.real) + abs(loc.imag)))
