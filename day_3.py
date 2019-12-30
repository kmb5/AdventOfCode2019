#import pygame
#from pygame.locals import QUIT
from PIL import Image, ImageDraw

def main():

    filename = 'inputs/day_3_input.txt'

    with open(filename) as f:
        puzzle_input = f.read().splitlines()
    
    solution_part_1 = part_1(puzzle_input)

    print(f'Part 1 solution: {solution_part_1}')
        
    
def part_1(puzzle_input):
    wire_1 = puzzle_input[0].split(',')
    wire_2 = puzzle_input[1].split(',')

    origin_point = (8500,16000) 
    # Arbitrary number so that the wires will
    # fit entriely on the image we generate at the end.
    # For sure there is a math way of calculating this but I could not figure out,
    # it was just trial and error until the whole image fit.

    path_1 = draw_path(wire_1, start_coordinates=origin_point)
    path_2 = draw_path(wire_2, start_coordinates=origin_point)

    result = list(set(path_1).intersection(path_2))
    index_of_origin = result.index(origin_point)
    result.pop(index_of_origin) # removing the intersection at origin point

    manhattans = []

    for i in result:
        '''Calculate Manhattan taxicab distance between each point and the origin'''
        distance = abs((origin_point[0] - i[0])) + abs((origin_point[1] - i[1]))
        manhattans.append(distance)

    smallest_dist = min(manhattans) # This is our solution

    ''' This is only needed to render an image with the paths,
    it is not a requirement for solving the case!'''

    img = Image.new('RGB', ((15000,19000)))
    # Again an arbitrary image size so that everything fits
    ImageDraw.Draw(img).point(path_1, fill='red')
    ImageDraw.Draw(img).point(path_2, fill='yellow')
    img.save('day_3_visualisation.jpg')

    return smallest_dist

def draw_path(wire_path: list, start_coordinates: tuple) -> list:

    path = [] 
    path.append(start_coordinates)
    # Initializing the path with the starting coordinates

    for instruction in wire_path:

        direction = instruction[0]
        distance = int(instruction[1:])
        prev_point_x = path[-1][0]
        prev_point_y = path[-1][1]

        if direction == 'L':
            new_points = [(prev_point_x - x, prev_point_y) for x in range(1, distance + 1)]
        elif direction == 'R':
            new_points = [(prev_point_x + x, prev_point_y) for x in range(1, distance + 1)]
        elif direction == 'U':
            new_points = [(prev_point_x, prev_point_y + y) for y in range(1, distance + 1)]
        elif direction == 'D':
            new_points = [(prev_point_x, prev_point_y - y) for y in range(1, distance + 1)]
        
        path.extend(new_points)

    return path

if __name__ == '__main__':
    main()