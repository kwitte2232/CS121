import sys


def negate_values(l):

    negative_l = []
    if len(l) == 0:
        #print('EMPTY')
        return "EMPTY", negative_l
    for item in l:
        negative = -1*item
        negative_l.append(negative)

    return negative_l


# Implement a function called negate_values here
# This function takes a list of integers, and returns
# a *new* list with the values of the list negated.


#if __name__ == "__main__":
    # parse the input
    #tokens = sys.stdin.read().split()
    #n = int(tokens.pop(0))
   # l = [int(item.strip()) for item in tokens]
   # assert len(l) == n

   # l_copy = l[:]

    # Replace l with a call to your negate_values function
    # Variable l contains the list of integers.
   # rv = l

   # if l != l_copy:
       # raise ValueError("Don't modify the list you pass to negate_values!")

   # if len(l) > 0:
        #print(" ".join([str(x) for x in rv]))
   # else:
       # print("EMPTY")
