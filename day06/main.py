with open('input.txt', 'r') as input_file:
    lines = input_file.read()

groups = [set(list(line.replace('\n', ''))) for line in lines.split('\n\n')]

question_sum = 0
for group in groups: question_sum += len(group)
print(question_sum)

groups = [[set(person) for person in line.split('\n')] for line in lines.strip().split('\n\n')]

question_sum = 0
for group in groups: question_sum += len(set.intersection(*group))
print(question_sum)
