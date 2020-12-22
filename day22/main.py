from copy import deepcopy

with open('input.txt', 'r') as input_file:
    lines = input_file.read().strip().split('\n\n')

players = {}
for line in lines:
    line = line.split('\n')
    players[line[0].strip(':')] = [int(card) for card in line[1:]]

def get_deck_hash(deck):
    index, total = 1, 0
    for card in reversed(deck):
        total += index * card
        index += 1
    return total

def combat(p, is_recursive=False):
    states = set()
    while True:
        new_state = (get_deck_hash(p['Player 1']), get_deck_hash(p['Player 2']))
        if new_state in states and is_recursive: return ('Player 1', p['Player 1'])
        states.add(new_state)

        p1_card = p['Player 1'].pop(0)
        p2_card = p['Player 2'].pop(0)

        if p1_card <= len(p['Player 1']) and p2_card <= len(p['Player 2']) and is_recursive:
            sub_winner = combat({
                'Player 1' : p['Player 1'][:p1_card],
                'Player 2' : p['Player 2'][:p2_card],
            }, is_recursive=True)

            local_winner = sub_winner[0]
        else:
            if p1_card > p2_card: local_winner = 'Player 1'
            else: local_winner = 'Player 2'

        if local_winner == 'Player 1':
            p['Player 1'].append(p1_card)
            p['Player 1'].append(p2_card)
        else:
            p['Player 2'].append(p2_card)
            p['Player 2'].append(p1_card)
        
        if len(p['Player 1']) == 0: return ('Player 2', p['Player 2'])
        elif len(p['Player 2']) == 0: return ('Player 1', p['Player 1'])


winner = combat(deepcopy(players))
print(get_deck_hash(winner[1]))
winner = combat(deepcopy(players), is_recursive=True)
print(get_deck_hash(winner[1]))
