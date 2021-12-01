lines = open('day_1/input.txt', 'r').read().splitlines()

increase_count = 0
decrease_count = 0

num_lines = [int(line) for line in lines]
prev = -1
for i, num in enumerate(num_lines):
    if i > len(num_lines) - 3:
        break

    window_sum = num + num_lines[i+1] + num_lines[i+2]

    if prev != -1:
        if prev < window_sum:
            increase_count += 1
        elif prev > window_sum:
            decrease_count += 1
    prev = window_sum


print(f'Total lines: {len(num_lines)}')
print(f'Total increases: {increase_count}')
print(f'Total decreases: {decrease_count}')