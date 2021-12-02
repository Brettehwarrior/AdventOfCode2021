lines = open('day_2/input.txt', 'r').read().splitlines()

commands = []
for line in lines:
    line = line.split()
    commands.append((line[0], int(line[1])))
    
    
h_pos = 0
depth = 0
aim = 0

for command in commands:
    if command[0] == 'forward':
        h_pos += command[1]
        depth += aim * command[1]
    elif command[0] == 'down':
        aim += command[1]
    elif command[0] == 'up':
        aim -= command[1]
        

print(f'Horizontal position: {h_pos}')
print(f'Depth: {depth}')
print(f'Product: {h_pos * depth}')
