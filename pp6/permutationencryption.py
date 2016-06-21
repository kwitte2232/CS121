import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/permutationencryption
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def encrypt(string, perm):
    '''
    Takes a string and a list with the keys for the permutation
    Returns the permutation

    Inputs:
        string: a string
        perm: a list 

    Returns:
        A string with the permuted message
    '''

    n = len(perm)
    end = len(string) -1
    substrings = []
    ss = ''
    for i, letter in enumerate(string):
        ss = ss + letter
        if len(ss) == n:
            substrings.append(ss)
            ss = ''
        if i == end:
            while len(ss)%n != 0:
                ss = ss + ' '
            substrings.append(ss)

    print(substrings)

    swapped = []
    for sub in substrings:
        swap_string = [0]*n
        swap_indices = {}
        for i, letter in enumerate(sub):
            new_dex = perm[i] - 1
            swap_indices[new_dex] = letter
        for dex in swap_indices:
            swap_string[dex] = swap_indices[dex]
        new_string = ''.join(swap_string)
        swapped.append(new_string)

    perm_string = ''.join(swapped)

    return perm_string


if __name__ == "__main__":
    tokens = sys.stdin.readline().split()

    while int(tokens[0]) != 0:
        n = int(tokens[0])
        permutations = [int(x) for x in tokens[1:]]
        assert(len(permutations) == n)

        message = sys.stdin.readline().strip()
    
        print("'{}'".format(encrypt(message, permutations)))
        
        tokens = sys.stdin.readline().split()
    
