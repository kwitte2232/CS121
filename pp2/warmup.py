def F1(i, j) :
    print("F1({}, {})".format(i, j))
    #prints as a string F1(i, j)
    F2(j, i+j) #calling the function F2
    print("F1: i = {}, j = {}".format(i, j))
    #prints as a string "F1: i = "
    

def F2(i, j) :
    print("    F2({}, {})".format(i, j))
    k = F3(i, j) #calling the function F3
    print("    F2: i = {}, j = {}, k = {}".format(i, j, k))
    

def F3(i, j) :
    print("        F3({}, {})".format(i, j))
    i = i+j
    j = i+2*j
    k = 2*i+3*j
    print("        F3: i = {}, j = {}, k = {}".format(i, j, k))
    return k
    

print("Warmup exercise 1:")
F1(1, 1)
print()
print()


def mystery1(l):
    rv = []
    for x in l:
        rv = [x] + rv
    return rv

print("Warmup exercise 2:")
l = [0, 1, 2, 3, 4]
nl = mystery1(l)
print("l: ", l)
print("nl: ", nl)
print()
print()

def mystery2(l):
    rv = []
    for i in range(len(l)-1, -1, -1):
        #end at -1? What does that mean? The end is EXCLUSIVE.
        #So it actually ends at 0
        # The range is actually from 4 to 0 (5 eleemtns) if len of l = 5
        # the last -1 is the incrementer
        rv.append(l[i])
    return rv

print("Warmup exercise 3:")
l = [0, 1, 2, 3, 4]
nl = mystery2(l)
print("l: ", l)
print("nl: ", nl)
print()
print()

def mystery3(l):
    n = len(l)
    for i in range(n // 2):
        # The // means to divide with the intregral result (discard R)
        t = l[i]
        l[i] = l[n-i-1]
        l[n-i-1] = t
        # This loop swaps the elements in the list, working from outside in
        # len = 6, 5 and 0 swap, 4 and 1 swap, 2 and 3 swap

# def mysteries 1,2,3 were all ways to invert the input list
# there is a list method, list.reverse(), that does the exact same thing

print("Challenge exercise:")
l = [0, 1, 2, 3, 4]
mystery3(l)
print("l: ", l)
print()
print()
