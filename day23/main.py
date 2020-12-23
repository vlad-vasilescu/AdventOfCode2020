with open('input.txt', 'r') as input_file:
    line = input_file.read().strip()

cups_list = [int(cup) for cup in line] + [i for i in range(10, 1000001)]
next_cups = {}
for i in range(len(cups_list)):
    if i == len(cups_list) - 1: next_cups[cups_list[i]] = cups_list[0]
    else: next_cups[cups_list[i]] = cups_list[i + 1]

max_val = max(cups_list)
min_val = min(cups_list)

current = cups_list[0]
for move in range(10000000):
    first_next = next_cups[current]
    second_next = next_cups[first_next]
    third_next = next_cups[second_next]

    next_cups[current] = next_cups[third_next]

    search = current
    while search == current or search == first_next or search == second_next or search == third_next:
        search -= 1
        if search < min_val: search = max_val

    after_search = next_cups[search]
    next_cups[search] = first_next
    next_cups[third_next] = after_search
    
    current = next_cups[current]

# def parse(node, path=[]):
#     if node not in path:
#         path.append(node)
#         return parse(next_cups[node], path)
#     else: return path

# print(*parse(1)[1:], sep='')

print(next_cups[1] * next_cups[next_cups[1]])
