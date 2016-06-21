import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/flowlayout
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes two parameters:
#
#  - max_width: The maximum width of the window
#  - rectangles: A list of pairs. Each pair contains two integers:
#                the width and height of a rectangle
#
# You must return the width and height of the resulting window.

class Rectangle(object):
    
    def __init__(self, dimensions):
        self._width = dimensions[0]
        self._height = dimenstions[1]

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    def __repr__(self):
        return "width: {}, height: {}".format(self._width,
            self._height)


def solve(max_width, rectangles):
    # YOUR CODE HERE

    rects = [list(rectangle) for rectangle in rectangles]

    rect_objs = []
    for r in rects:
        rect = Rectangle(r)
        rect_objs.append(rect)

    
    # Replace 0, 0 with the width and height of the resulting window.
    return 0, 0


#if __name__ == "__main__":
    #tokens = sys.stdin.read().strip().split()

   # width = int(tokens.pop(0))
    #while width != 0:
        #rectangles = []
        #rwidth = int(tokens.pop(0))
        #rheight = int(tokens.pop(0))
        #while rwidth != -1 and rheight != -1:
            #rectangles.append( (rwidth, rheight) )
            #rwidth = int(tokens.pop(0))
            #rheight = int(tokens.pop(0))
            
        #w, h = solve(width, rectangles)
        #print("{} x {}".format(w, h))

        #width = int(tokens.pop(0))
