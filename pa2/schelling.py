#  CS121: Schelling Model of Housing Segregation
#
#   Program for simulating of a variant of Schelling's model of
#   housing segregation.  This program takes four parameters:
#    
#    filename -- name of a file containing a sample grid
#
#    R - The radius of the neighborhood: home (i, j) is in the
#        neighborhood of home (k,l) if |k-i| + |l-j| <= R.
#
#    threshold - minimum acceptable threshold for ratio of neighbor
#    value to the total number of homes in his neighborhood.
#
#    max_steps - the maximum number of passes to make over the
#    neighborhood during a simulation.
#
#  Sample use:python schelling.py tests/grid4.txt 1 0.51 3
#

#Name: Kristen Witte

import os
import sys
import utility


def convert_to_tuples(grid):
    '''
    Generate a grid with coordinates

    Inputs:
        grid: the grid

    Returns:
        grid_coord: a list of tuples that are coordinates
    '''

    n = len(grid)

    grid_coords = []
    for i in range(n):
        grid_coords.append([0]*n)

    for i in range(n):
        for j in range(n):
            tup = (i, j)
            grid_coords[i][j] = tup

    return grid_coords


def find_opens(grid, grid_coords):
    '''
    Finds the open positions in the grid

    Inputs:
        grid: the grid
        grid_coords: list of tuples of the coordinates

    Returns:
        open_coords: a list of the open coordinates as tuples
    '''


    n = len(grid)

    open_coords = []
    row_num = 0
    counter = 0
    for row in grid:
        for dex, space in enumerate(row):
            if space == "O":
                indices = []
                indices.append(dex)
                for dx in indices:
                    coord = grid_coords[row_num][dx]
                    open_coords.append(coord)
        row_num = row_num + 1

    return open_coords


def make_neighborhood(grid, location_coord, R):
    '''
    Generate the neighborhood around the active coordinate

    Inputs:
        grid: the grid
        location_coord: the active coordinate
        R: threshold

    Returns:
        nh_coord: a list of coordinates making up the neighborhood
    '''

    n = len(grid)
    nh_coord = []
    i = location_coord[0]
    j = location_coord[1]

    for k in range(n):
        for l in range(n):
            value = abs(k-i) + abs(l-j)
            if value <= R:
                nh_locn = (k, l)
                nh_coord.append(nh_locn)

    return nh_coord


def get_curr_type(grid, location):
    '''
    get the current type from the grid

    Inputs:
        grid: the grid
        location: the active coordinate

    Returns:
        curr_type: as a string, "B", "R", or "O"
    '''

    a = location[0]
    b = location[1]
    curr_type = grid[a][b]

    return curr_type


def is_curr_type_satisfied(grid, R, threshold, location, curr_type):
    ''' 
    Is the homeowner at the specified location satisfied?

    Inputs: 
        grid: the grid
        R: radius for the neighborhood
        threshold: satisfaction threshold
        location: a grid location
        curr_type: input the current type to provide wider usage
            of the function
      
    Returns: 
        True: if the location's satisfaction score is at or 
            above the threshold
        False: if the location's satisfaction score is below
            the threshold
    '''
    status = True
    nh = make_neighborhood(grid, location, R)
    total = len(nh)

    sames = 0
    nh_opens = 0

    for i in nh:
        curr_neighbor = list(i)
        x = curr_neighbor[0]
        y = curr_neighbor[1]
        neighbor_type = grid[x][y]

        if curr_type == neighbor_type:
            sames = sames + 1

        if neighbor_type == "O":
            nh_opens = nh_opens + 1

    sat_score = (sames + 0.5*(nh_opens))/total

    if sat_score < threshold:
        status = False

    return status

def is_satisfied(grid, R, threshold, location):
    ''' 
    Is the homeowner at the specified location satisfied?

    Inputs: 
        grid: the grid
        R: radius for the neighborhood
        threshold: satisfaction threshold
        location: a grid location
      
    Returns: 
        True: if the location's satisfaction score is at or 
            above the threshold
        False: if the location's satisfaction score is below
            the threshold
    '''

    status = True
    nh = make_neighborhood(grid, location, R)
    location = list(location)
    a = location[0]
    b = location[1]
    curr_type = grid[a][b]
    total = len(nh)

    sames = 0
    nh_opens = 0

    for i in nh:
        curr_neighbor = list(i)
        x = curr_neighbor[0]
        y = curr_neighbor[1]
        neighbor_type = grid[x][y]

        if curr_type == neighbor_type:
            sames = sames + 1

        if neighbor_type == "O":
            nh_opens = nh_opens + 1

    sat_score = (sames + 0.5*(nh_opens))/total

    if sat_score < threshold:
        status = False

    return status

def detm_unsatisfied(grid, R, threshold):
    ''' 
    Determine the unsatisfied homes in the neighborhood

    Inputs: 
        grid: the grid
        R: radius for the neighborhood
        threshold: satisfaction threshold
      
    Returns: 
        unsat_coords: a list of coordinates for the unsatisfied
            homes in the grid
    '''

    n = len(grid)

    unsat_coords = []

    for i in range(n):
        for j in range(n):
            location = [i, j] 
            curr_type = get_curr_type(grid, location)
            if curr_type == 'R' or curr_type == 'B':
                status = is_curr_type_satisfied(grid, R, threshold, location, curr_type)
                if status == False:
                    coords = tuple(location)
                    unsat_coords.append(coords)

    return unsat_coords

def query_open(grid, grid_coords, unsat_list, opens_list,
    R, threshold, us, curr_type):
    ''' 
    Is a homeoner satisfied in one of the open positions?

    Inputs: 
        grid: the grid
        grid_coords: list of list tuples of the coordinates
        unsat_list: list of the unsatisfied coordinates as lists,
            rather than tuples
        opens_list: list of the open coordinates as lists,
            rather than tuples
        R: radius for the neighborhood
        threshold: satisfaction threshold
        us: active unsatisfied homeowner as its coordinate
        curr_type: type of the active unsatisfied homeowner
      
    Returns: 
        grid: the grid (with relocations)
        unsat_list: a list of coordinates for the unsatisfied
            homes, as list of lists, in the grid after relocation
        opens_lists: list of the open coordinates as lists,
            rather than tuples, after the relocation
        relocn: 
            True, if a relocation occurred
            False, if a relocation didn't occur
    '''

    relocn = True

    for op in opens_list:
        temp_status = is_curr_type_satisfied(grid, R, threshold, 
            op, curr_type)
        if temp_status == True:
            grid, unsat_list, opens_list = relocate(grid, unsat_list,
                opens_list, us, curr_type, op)
            break
        else:
            relocn = False
    
    return grid, unsat_list, opens_list, relocn


def my_test(grid, R, threshold):

    grid_coords = convert_to_tuples(grid)
    open_coords = find_opens(grid, grid_coords)
    unsat_coords = detm_unsatisfied(grid, R, threshold)

    opens_list = [list(opens) for opens in open_coords]
    unsat_list = [list(unsats) for unsats in unsat_coords]

    return grid_coords, opens_list, unsat_list


def relocate(grid, unsat_list, opens_list, us, curr_type, op):
    ''' 
    Relocate an unsatisfied homeowner

    Inputs: 
        grid: the grid
        unsat_list: list of the unsatisfied coordinates as lists,
            rather than tuples
        opens_list: list of the open coordinates as lists,
            rather than tuples
        R: radius for the neighborhood
        threshold: satisfaction threshold
        us: active unsatisfied homeowner as its coordinate
        curr_type: type of the active unsatisfied homeowner
        op: the destination coordinate for the relocation
      
    Returns: 
        grid: the grid (with relocations)
        unsat_list: a list of coordinates for the unsatisfied
            homes in the grid after relocation
        opens_lists: list of the open coordinates as lists,
            rather than tuples, after the relocation
    '''

    us_dex = unsat_list.index(us)
    del unsat_list[us_dex]
    op_dex = opens_list.index(op)
    del opens_list[op_dex]
    opens_list.insert(0, us)

    n = len(grid)

    for i in range(n):
        if i == op[0]:
            row = grid[i]
            row.pop(op[1])
            row.insert(op[1], curr_type)

    for i in range(n):
        if i == us[0]:
            row = grid[i]
            row[us[1]] = "O"

    return grid, unsat_list, opens_list 

def query_all(grid, grid_coords, unsat_list, opens_list, R, threshold):
    ''' 
    Iterate through the list of unsatisfieds homeowners for relocation

    Inputs: 
        grid: the grid
        grid_coords: list of list tuples of the coordinates
        unsat_list: list of the unsatisfied coordinates as lists,
            rather than tuples
        opens_list: list of the open coordinates as lists,
            rather than tuples
        R: radius for the neighborhood
        threshold: satisfaction threshold
      
    Returns: 
        grid: the grid (with relocations)
        exit: 
            True, if no more relocations occurred
            False, if relocations can occur
    '''

    count = 0
    exit = False

    n = len(unsat_list)
    print(unsat_list)

    x = unsat_list[:]

    for i in range(0,n):
        us = x[0]
        curr_type = get_curr_type(grid, us)
        if count == 0:
            grid, unsat_list, opens_list, 
            relocn = query_open(grid, grid_coords, unsat_list, 
                opens_list, R, threshold, us, curr_type)
            if relocn == False:
                exit = True
            del x[0]
        if count >= 1:
            us = x[0]
            curr_type = get_curr_type(grid, us)
            for op in opens_list:
                new_status = is_curr_type_satisfied(grid, R, threshold, 
                    op, curr_type)
                if new_status == False:
                    grid, x, opens_list, 
                    relocn = query_open(grid, grid_coords, x, 
                        opens_list, R, threshold, us, curr_type)
                    if relocn == False:
                        exit = True
                else:
                    del x[0]
        count = count + 1

    return grid, exit

def do_simulation(grid, R, threshold, max_steps):
    ''' 
    Do a full simulation.
    
    Inputs:
        grid: the grid
        R: radius for the neighborhood
        threshold: satisfaction threshold
        max_steps: maximum number of steps to doccd 

    Returns:
        num_steps: number of steps executed.
    '''
    
    num_steps = 0

    grid_coords = convert_to_tuples(grid)

    for step in range(0, max_steps):
        open_coords = find_opens(grid, grid_coords)
        unsat_coords = detm_unsatisfied(grid, R, threshold)

        opens_list = [list(opens) for opens in open_coords]
        unsat_list = [list(unsats) for unsats in unsat_coords]

        grid, exit = query_all(grid, grid_coords, unsat_list,
            opens_list, R, threshold)

        num_steps = num_steps + 1
        if exit == True:
            break

    print(grid)
    return num_steps
        
    
def go(args):
    usage = "usage: python schelling.py <grid file name> <R > 0> <0 < threshold <= 1.0> <max steps >= 0>\n"
    grid = None
    threshold = 0.0
    R = 0
    max_steps = 0
    MAX_SMALL_GRID = 20

    
    if (len(args) != 5):
        print(usage)
        sys.exit(0)

    # parse and check the arguments
    try:
        grid = utility.read_grid(args[1])

        R = int(args[2])
        if R <= 0:
            print("R must be greater than zero")
            sys.exit(0)

        threshold = float(args[3])
        if (threshold <= 0.0 or threshold > 1.0):
            print("threshold must be between 0.0 and 1.0 not inclusive")
            sys.exit(0)

        max_steps = int(args[4])
        if max_steps <= 0:
            print("max_steps must be greater than or equal to zero")
            sys.exit(0)

    except:
        print(usage)
        sys.exit(0)
        

    num_steps = do_simulation(grid, R, threshold, max_steps)
    if len(grid) < MAX_SMALL_GRID:
        for row in grid:
            print(row)
    else:
        print("Result grid too large to print")

    print("Number of steps simulated: " + str(num_steps))

if __name__ == "__main__":
    go(sys.argv)

