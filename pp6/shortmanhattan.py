#!/usr/bin/python3

import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/shortmanhattan
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the find_paths() function.  Do not
# modify any other code.

# This function takes four parameters: x0, y0, x1, y1 (as defined
# in the problem statement)
#
# The function must return a list of all the shortest paths from (x0,y0) to
# (x1, y1). For example:
#
#    find_paths(0,0,1,1) would return [["right", "up"], ["up", "right"]]
#    find_paths(1,1,0,0) would return [["left", "down"], ["down", "left"]]
#
# Note: The order of the paths is not important. e.g., the first call could
#       return [["up", "right"], ["right", "up"]] and it would also be correct.
#
# Note (2): If there are no shortest paths (because you're finding the path from
#           one point to itself, the function must return [[]] (i.e., a list with
#           just one path: the empty path.
def find_paths(x0,y0,x1,y1):

    if x1 == x0 and y1 == y0:
        return "None"

    x_dist = abs(x1 - x0) #number of steps taken
    y_dist = abs(y1 - y0)

    if x1 < x0:
        x_direction = 'left'
    if x1 > x0:
        x_direction = 'right'
    if x1 == x0:
        x_direction = None
    

    if y1 < y0:
        y_direction = 'down'
    if y1 > x0:
        y_direction = 'up'
    if y1 == y0:
        y_direction = None

    x_move = []
    for i in range(x_dist):
        x_move.append(x_direction)

    y_move = []
    for i in range(y_dist):
        y_move.append(y_direction)

    move = x_move + y_move
    print(move)
    final = helper_moves(move)

    return final

def helper_moves(move):

    if len(move) == 1:
        #base case
        return [move]
    else:
        rv = []
        for i, m in enumerate(move):
            sub_move = move[:]
            del sub_move[i]
            all_moves = helper_moves(sub_move)
            for a in all_moves:
                current_move = [m] + a
                if current_move not in rv:
                    #Deal with the duplicates generated by the duplicates
                        #in the entry
                    rv.append(current_move)
        return rv

#if __name__ == "__main__":
    #x0, y0, x1, y1 = sys.stdin.read().split()

    #paths = find_paths(int(x0), int(y0), int(x1), int(y1))

    #if len(paths) == 1 and len(paths[0]) == 0:
        #print("NONE")
   # else:
        #for p in paths:
            #print(" ".join(p))

    
