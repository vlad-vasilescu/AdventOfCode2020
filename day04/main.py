from copy import copy
from collections import Counter
import re

all_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def validate_data(passport):
    if not Counter(passport.keys()) == Counter(required) and \
        not Counter(passport.keys()) == Counter(all_fields):
        return False

    if not 1920 <= int(passport['byr']) <= 2002: return False
    if not 2010 <= int(passport['iyr']) <= 2020: return False
    if not 2020 <= int(passport['eyr']) <= 2030: return False
    if passport['hgt'][-2:] == 'cm':
        if not 150 <= int(passport['hgt'][:-2]) <= 193: return False
    elif passport['hgt'][-2:] == 'in':
        if not 59 <= int(passport['hgt'][:-2]) <= 76: return False
    else: return False
    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']): return False
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
    if not re.fullmatch(r'[0-9]{9}', passport['pid']): return False

    return True


with open('input.txt', 'r') as input_file:
    lines = input_file.read().strip().split('\n\n')
    lines = [line.replace('\n', ' ') for line in lines]

no_valid = 0
for line in lines:
    fields = {}
    for attr in line.split(' '):
        attr_name = attr.split(':')[0]
        attr_val = attr.split(':')[1]
        fields[attr_name] = attr_val

    if validate_data(fields): no_valid += 1

print(no_valid)
