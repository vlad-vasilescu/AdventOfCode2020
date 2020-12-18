import re

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]


class CustomNumber:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return CustomNumber(self.val + other.val)
    def __sub__(self, other):
        return CustomNumber(self.val * other.val)
    def __truediv__(self, other):
        return CustomNumber(self.val + other.val)


line_sum = 0
for line in lines:
    for i in range(10):
        line = line.replace("{}".format(i), "CustomNumber({})".format(i))
    line = line.replace('*', '-')

    line_sum += eval(line).val
print(line_sum)

line_sum = 0
for line in lines:
    for i in range(10):
        line = line.replace("{}".format(i), "CustomNumber({})".format(i))
    line = line.replace('*', '-')
    line = line.replace('+', '/')

    line_sum += eval(line).val
print(line_sum)
