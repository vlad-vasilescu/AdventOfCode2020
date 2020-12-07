import re

with open('input.txt', 'r') as input_file:
    lines = [line.replace('bags.', '') for line in input_file.readlines()]
    lines = [line.strip() for line in lines]

bags = {}
for line in lines:
    line = line.split(' bags contain ')
    parent_bag = line[0]
    children_bags = line[1]
    
    if children_bags == 'no other':
        bags[parent_bag] = [[0, children_bags]]
    else:
        children_bags = children_bags.split(', ')
        bags[parent_bag] = [[int(bag.split(' ')[0]), re.sub(r'\d+ ', '', bag.replace(' bags', '').replace(' bag', '').strip('.'))] for bag in children_bags]

def can_hold_bag(search_bags, wanted_bag):
    new_search = []
    for bag, children in bags.items():
        if bag not in search_bags: continue
        for child in children:
            if child[1] == wanted_bag: return True
            new_search.append(child[1])
    if len(new_search): return can_hold_bag(new_search, wanted_bag)
    return False

can_hold = 0
for bag in bags:
    if can_hold_bag([bag], 'shiny gold'): can_hold += 1
print(can_hold)

def bags_within(search_bag, multiplier):
    bag_count = 0
    for bag, children in bags.items():
        if bag not in search_bag: continue
        for child in children:
            if child[0] == 0: continue
            bag_count += (child[0] * multiplier) + bags_within(child[1], child[0] * multiplier)

    return bag_count

print(bags_within('shiny gold', 1))
