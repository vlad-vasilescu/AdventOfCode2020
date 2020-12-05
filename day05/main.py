def minimize_range(range_begin, range_end, lh_code, uh_code, code):
    for char in code:
        mid_point = (range_begin + range_end) // 2

        if char == lh_code: range_end = mid_point
        elif char == uh_code: range_begin = 1 + mid_point

    if range_begin == range_end: return range_begin
    else: return [range_begin, range_end]


with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

ids = []
for line in lines:
    row_num = minimize_range(0, 127, 'F', 'B', line[:7])
    col_num = minimize_range(0, 7, 'L', 'R', line[7:])

    seat_id = row_num * 8 + col_num    
    ids.append(seat_id)

print(max(ids))
[print(i) for i in range(max(ids), min(ids), -1) if i not in ids]
