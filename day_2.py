def main():

    filename = 'inputs/day_2_input.txt'

    with open(filename) as f:
        puzzle_input = f.read().split(',')

    puzzle_input = [int(x) for x in puzzle_input]

    puzzle_input_modified = puzzle_input[:]
    puzzle_input_modified[1] = 12
    puzzle_input_modified[2] = 2

    part_1_solution = part_1(puzzle_input_modified)
    print(f'Part 1 solution: {part_1_solution}')

    part_2_noun_verb = part_2(puzzle_input)
    part_2_solution = 100 * part_2_noun_verb[0] + part_2_noun_verb[1]
    print(f'Part 2 solution: {part_2_solution}')

def part_1(puzzle_input):

    memory = puzzle_input[:]
    instructions = list(chunks(puzzle_input, 4))

    result_memory = run_computer(instructions, memory)
    
    return(result_memory[0])

def part_2(puzzle_input):
    
    memory = puzzle_input[:]

    for i in range(100):
        for j in range(100):
            memory[1] = i
            memory[2] = j

            instructions = list(chunks(memory, 4))
            result_memory = run_computer(instructions, memory)

            if result_memory[0] == 19690720:
                return (i, j)
            else:
                # Reset the memory before the loop starts again
                memory = puzzle_input[:]

def chunks(lst: list, n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def run_computer(list_of_instructions, memory):
    '''Execute a list of instructions and return the memory
    after the last instruction is finished, or the program encountered an opcode 99'''

    for instruction in list_of_instructions:

        if instruction[0] != 99:
            try:
                run_opcode(instruction, memory)
            except ValueError as e:
                print(e)
        else:
            break

    return memory

def run_opcode(instruction: list, memory: list) -> list:
    '''Execute an instruction (which is a list of 4 elements - opcode & 3 positions),
    then overwrite and return the memory inputted depending on the instruction.'''

    opcode = instruction[0]

    if opcode not in [99, 1, 2]:
        raise ValueError('Unknown opcode')

    pos1 = instruction[1]
    pos2 = instruction[2]
    result_pos = instruction[3]

    if opcode == 99:
        print('Opcode 99 - program halted.')
        return memory

    elif opcode == 1:
        memory[result_pos] = memory[pos1] + memory[pos2]
        return memory

    elif opcode == 2:
        memory[result_pos] = memory[pos1] * memory[pos2]
        return memory

if __name__ == '__main__':
    main()