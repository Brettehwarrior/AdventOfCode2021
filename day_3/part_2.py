lines = open('day_3/input_ex.txt', 'r').read().splitlines()

bit_string_len = len(lines[0])

def update_totals(lines:list):
    totals = [0] * bit_string_len
    for line in lines:
        for i in range(bit_string_len):
            totals[i] += int(line[i])
    return totals

def cull_lines(lines:list, match:str, index:int):
    return [line for line in lines if not line[index] == match]

# Find oxygen thing
for i in range(bit_string_len-1):
    totals = update_totals(lines)
    lines = cull_lines(lines, '0' if totals[i] > len(lines) // 2 else '1', i)
oxygen_generator_rating = int(str(max([int(line) for line in lines])), 2)

# Now it's funny CO2 time
lines_new = open('day_3/input_ex.txt', 'r').read().splitlines()

# Find er
for i in range(bit_string_len-1):
    totals = update_totals(lines_new)
    if totals[i] > len(lines_new) // 2:
        lines_new = cull_lines(lines_new, '1', i)
    elif totals[i] < len(lines_new) // 2:
        lines_new = cull_lines(lines_new, '0', i)
    else:
        break
co2_scrubber_rating = int(str(min([int(line) for line in lines_new])), 2)

print(f'Oxygen: {oxygen_generator_rating}')
print(f'CO2: {co2_scrubber_rating}')
print(f'Product: {oxygen_generator_rating * co2_scrubber_rating}')