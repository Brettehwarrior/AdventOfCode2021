lines = open('day_3/input.txt', 'r').read().splitlines()

bit_string_len = len(lines[0])

def update_totals():
    totals = [0] * bit_string_len
    for line in lines:
        for i in range(bit_string_len):
            totals[i] += int(line[i])
    return totals

def cull_lines(lines:list, match:str, index:int):
    return [line for line in lines if not line[index] == match]
    

# Find oxygen thing
for i in range(bit_string_len):
    totals = update_totals()
    lines = cull_lines(lines, '0' if totals[i] > len(lines) // 2 else '1', i)

oxygen_generator_rating = max([int(line) for line in lines])
print(oxygen_generator_rating)