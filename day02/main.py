with open('input.txt', 'r') as input_file:
    lines = [line.strip().split(': ') for line in input_file.readlines()]

valid = 0
for line in lines:
    valid_appr = [int(appr) for appr in line[0].split(' ')[0].split('-')]
    char = line[0].split(' ')[1]
    string = line[1]
    
    # appr = string.count(char)
    # if valid_appr[0] <= appr <= valid_appr[1]: valid += 1

    first_pos = string[valid_appr[0] - 1] == char
    second_pos = string[valid_appr[1] - 1] == char
    if first_pos != second_pos: valid += 1

print(valid)
