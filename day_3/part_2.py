import copy
import numpy as np

lines = open('day_3/input.txt', 'r').read().splitlines()
bit_string_len = len(lines[0])


def get_totals(lines:list):
    totals = np.full((bit_string_len, 2), 0) # List of totals lists, first value being 0s total and second being 1s total

    for line in lines:
        for i in range(len(line)):
                totals[i][int(line[i])] += 1
    
    return totals

def cull_list(lines:list, index:int, target:str):
    culled_list = copy.deepcopy(lines)
    to_cull = [] # indices to cull
    
    # Find items to remove
    for i, line in enumerate(culled_list):
        if line[index] == target:
            to_cull.append(i)
            
    # Return with items removed
    return [item for i, item in enumerate(culled_list) if not i in to_cull]

def get_oxygen_generator_rating(lines:list):
    for i in range(bit_string_len):
        if len(lines) < 2:
            break
        
        totals = get_totals(lines)
        
        if totals[i][0] > totals[i][1]: 
            lines = cull_list(lines, i, '1')
        elif totals[i][0] < totals[i][1]:
            lines = cull_list(lines, i, '0')
        else: # For oxygen generator rating, cull 0s when equal
            lines = cull_list(lines, i, '0')
    
    return int(lines[0], 2)

def get_co2_scrubber_rating(lines:list):
    for i in range(bit_string_len):
        if len(lines) < 2:
            break

        totals = get_totals(lines)

        if totals[i][0] > totals[i][1]:
            lines = cull_list(lines, i, '0')
        elif totals[i][0] < totals[i][1]:
            lines = cull_list(lines, i, '1')
        else:  # For CO2 scrubber rating, cull 1s when equal
            lines = cull_list(lines, i, '1')

    return int(lines[0], 2)

if __name__ == '__main__':
    my_lines = copy.deepcopy(lines)

    oxygen_generator_rating = get_oxygen_generator_rating(my_lines)
    co2_scrubber_rating = get_co2_scrubber_rating(my_lines)

    print(f'Oxygen: {oxygen_generator_rating}')
    print(f'CO2: {co2_scrubber_rating}')
    print(f'Product: {oxygen_generator_rating * co2_scrubber_rating}')
