import math

# Function counts floor area.
def floor_area(width, height):

    f_area = width * height

    return f_area

# Function counts tile area.
def tile_surface(t_width, t_height):

    tile_area = t_height * t_width

    return tile_area

# Function counts how many tiles we need and what is the summary cost.
def costs(floor_area, tile_area, tile_cost):
    tile_volume = floor_area / tile_area
    tile_volume = math.ceil(tile_volume) # Number of tiles must be an intefer
    all_cost = tile_volume * tile_cost
    return all_cost

width = int(input("Please enter floor width: "))
height = int(input("Please enter floor height: "))

t_width = int(input("Please enter tile width: "))
t_height = int(input("Please enter tile height: "))

tile_cost = int(input("Please enter cost of one tile: "))

f_area = floor_area(width, height)
t_area = tile_surface(t_width, t_height)

print(f"The whole costs of new floor is: {costs(f_area, t_area, tile_cost)}")
