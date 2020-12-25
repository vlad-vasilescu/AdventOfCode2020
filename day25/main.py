with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

card_key = int(lines[0])
door_key = int(lines[1])

subject_number = 7
value = 1
i = 1
while True:
    value *= subject_number
    value %= 20201227

    if value == card_key or value == door_key:
        loop_size = i
        loop_subject = value
        break
    i += 1

if loop_subject == card_key: loop_subject = door_key
else: loop_subject = card_key

value = 1
for i in range(loop_size):
    value *= loop_subject
    value %= 20201227

print(value)
