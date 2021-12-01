lines = open('day_1/input.txt', 'r').read().splitlines()

increase_count = 0
decrease_count = 0

num_lines = [int(line) for line in lines]
prev = -1
for num in num_lines:
    if prev != -1:
        if prev < num:
            increase_count += 1
        elif prev > num:
            decrease_count += 1
    prev = num


print(f'Total lines: {len(num_lines)}')
print(f'Total increases: {increase_count}')
print(f'Total decreases: {decrease_count}')