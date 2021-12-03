lines = open('day_3/input.txt', 'r').read().splitlines()

bit_string_len = len(lines[0])
totals = [0] * bit_string_len

for line in lines:
    for i in range(bit_string_len):
        totals[i] += int(line[i])

gamma = ''.join(['1' if n > len(lines) // 2 else '0' for n in totals])
epsilon = ''.join(['0' if c == '1' else '1' for c in gamma])

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f'Product: {gamma * epsilon}')