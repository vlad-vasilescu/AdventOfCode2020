with open('input.txt', 'r') as input_file:
    lines = input_file.read().strip().split('\n\n')

fields = {}
for field in lines[0].split('\n'):
    field = field.split(': ')
    field_name = field[0]
    
    fields[field_name] = []
    for field_range in field[1].split(' or '):
        field_range = [int(n) for n in field_range.split('-')]
        fields[field_name].append(field_range)


invalid_sum = 0
valid_tickets = []
for nearby_ticket in lines[2].split('\n'):
    if nearby_ticket == 'nearby tickets:': continue
    nearby_ticket = [int(prop) for prop in nearby_ticket.split(',')]

    is_valid_ticket = True
    for prop in nearby_ticket:
        is_valid = False
        for field in fields.values():
            for field_range in field:
                if prop in range(field_range[0], field_range[1] + 1):
                    is_valid = True
        if not is_valid:
            invalid_sum += prop
            is_valid_ticket = False
    if is_valid_ticket: valid_tickets.append(nearby_ticket)

print(invalid_sum)

def is_valid(number, ranges):
    for interval in ranges:
        if number in range(interval[0], interval[1] + 1):
            return True
    return False


field_possible = {}

for field_name, field_ranges in fields.items():
    field_possible[field_name] = []
    for i in range(len(fields)):
        is_field_valid = True
        for ticket in valid_tickets:
            if not is_valid(ticket[i], field_ranges): is_field_valid = False
        
        if is_field_valid: field_possible[field_name].append(i)


for i in range(20):
    for field_name, poss in field_possible.items():
        if len(poss) != 1: continue
        else:
            for other_name, other_poss in field_possible.items():
                if other_name != field_name and poss[0] in other_poss: other_poss.remove(poss[0])


my_ticket = [int(n) for n in lines[1].split('\n')[1].split(',')]
departure_prod = 1
for field_name, pos in field_possible.items():
    if 'departure' in field_name: departure_prod *= my_ticket[pos[0]]

print(departure_prod)
