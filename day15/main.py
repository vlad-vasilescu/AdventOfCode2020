with open('input.txt', 'r') as input_file:
    line = input_file.read().strip()

numbers = [int(num) for num in line.split(',')]
last_turn = {number: turn for turn, number in enumerate(numbers)}

new_number = numbers[-1]
for turn in range(len(numbers) - 1, 30000000):
    current = new_number

    if new_number not in last_turn: new_number = 0
    else: new_number = turn - last_turn[new_number]

    last_turn[current] = turn

print(current)
