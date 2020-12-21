import functools

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

ingredients = {}
alergens = {}
counts = {}

for line in lines:
    line = line.split('(')
    ingr = line[0].strip(' ').split(' ')
    algr = [alg.strip(',') for alg in line[1].strip(')').split(' ')[1:]]

    for ingredient in ingr:
        if ingredient not in ingredients: ingredients[ingredient] = {}
        for alergen in algr:
            if alergen not in ingredients[ingredient]: ingredients[ingredient][alergen] = 0
            ingredients[ingredient][alergen] += 1

    for alergen in algr:
        if alergen not in alergens: alergens[alergen] = {}
        for ingredient in ingr:
            if ingredient not in alergens[alergen] : alergens[alergen][ingredient] = 0
            alergens[alergen][ingredient] += 1

    for ingredient in ingr:
        if ingredient not in counts: counts[ingredient] = 0
        counts[ingredient] += 1

sorted_alergen = sorted(alergens.keys(), key=lambda alg: alergens[alg][sorted(alergens[alg], key=alergens[alg].get, reverse=True)[0]], reverse=True)

map_alergen = {}
for alergen in sorted_alergen:
    ingr = alergens[alergen]
    sorted_ingr = sorted(ingr, key=ingr.get, reverse=True)
    chosen_ingr = None
    
    for ingredient in sorted_ingr:
        if ingredient not in map_alergen.values():
            chosen_ingr = ingredient
            break
    map_alergen[alergen] = chosen_ingr

total_count = 0
for ingredient in ingredients:
    if ingredient not in map_alergen.values():
        total_count += counts[ingredient]

print(total_count)

ingr_list = ''
bad_alergens = list(map_alergen.keys())
bad_alergens.sort()

for alergen in bad_alergens:
    ingr_list += ',' + map_alergen[alergen]

ingr_list = ingr_list[1:]
print(ingr_list)
