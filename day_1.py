from math import floor

def find_fuel_for_module(mass: int) -> int:
    fuel = floor(mass / 3) - 2
    return fuel

def find_fuel_for_module_recursive(current_mass: int, total_mass: int=0) -> int:

    if current_mass <= 0:
        return total_mass

    else:
        fuel_need = find_fuel_for_module(current_mass)
        if fuel_need > 0:
            total_mass += fuel_need

        return find_fuel_for_module_recursive(fuel_need, total_mass)

def part_one(puzzle_input):
    
    total_fuel = 0

    for num in puzzle_input:
        total_fuel += find_fuel_for_module(num)

    return total_fuel

def part_two(puzzle_input):

    total_fuel = 0

    for num in puzzle_input:
        total_fuel += find_fuel_for_module_recursive(num)
    
    return total_fuel

def main():

    filename = 'inputs/day_1_input.txt'

    with open(filename) as f:
        puzzle_input = f.read().splitlines()

    puzzle_input = [int(x) for x in puzzle_input]

    part_one_solution = part_one(puzzle_input)
    print(f'Part one: {part_one_solution}')

    part_two_solution = part_two(puzzle_input)
    print(f'Part two: {part_two_solution}')

if __name__ == '__main__':
    main()