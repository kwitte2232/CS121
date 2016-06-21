import sys

# Implement a function called count_negative here
# This function takes a list of integers, and returns
# the number of negative integers in the list.

def count_negative(l):

    n = len(l)
    if n == 0:
        return []
    else:
        rv = []
        for item in l:
            if item < 0:
                rv.append(item)
        total_negatives = len(rv)

    return total_negatives


#if __name__ == "__main__":
    # parse the input
    #tokens = sys.stdin.read().split()
    #n = int(tokens.pop(0))
    #l = [int(item.strip()) for item in tokens]
    #assert len(l) == n

    # Replace 0 with a call to your count_negative function
    # Variable l contains the list of integers.
    #rv = 0

    #print(rv)
