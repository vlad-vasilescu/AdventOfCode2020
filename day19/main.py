import lark

with open('input.txt', 'r') as input_file:
    file = input_file.read().split('\n\n')
    lines = file[0]
    messages = file[1].strip('\n\n').split('\n')

grammar = lines.translate(str.maketrans('0123456789', 'abcdefghij'))
parser = lark.Lark(grammar, start='a')

count = 0
for msg in messages:
    try:
        parser.parse(msg)
        count += 1
    except: pass
print(count)


lines = lines.replace('8: 42', '8: 42 | 42 8')
lines = lines.replace('11: 42 31', '11: 42 31 | 42 11 31')
grammar = lines.translate(str.maketrans('0123456789', 'abcdefghij'))
parser = lark.Lark(grammar, start='a')

count = 0
for msg in messages:
    try:
        parser.parse(msg)
        count += 1
    except: pass
print(count)
