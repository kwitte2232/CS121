import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/quickbrownfox
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes one parameter: the phrase (as described in the problem statement)
#
# It must return a list of letters that are missing from the phrase (i.e., that 
# prevent the phrase from being a pangram, as described in the problem statement) 
# The missing letters should be reported in lower case and should be sorted 
# alphabetically.
#
# If the phrase is a pangram, just return an empty list.

ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

class Line(object):

    @staticmethod
    def replace(line):
        
        full_phrase = list(line)

        alpha_phrase = []

        for char in full_phrase:
            char = char.lower()
            if char in ALPHA:
                alpha_phrase.append(char)

        return alpha_phrase

    def __init__(self, line):
        self._alpha_phrase = Line.replace(line)

    @property
    def alpha_phrase(self):
        return self._alpha_phrase


def solve(phrase):
    
    for line in phrase:
        ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
        current_line = Line(line)
        for char in current_line.alpha_phrase:
            char = char.lower()
            if char in ALPHA:
                ALPHA.remove(char)
        if len(ALPHA) == 0:
            print("pangram")
        else:
            string = ""
            for char in ALPHA:
                string = string + char
            print('missing ' + string)




        #for char in ALPHA:
            #if char not in current_line.alpha_phrase:
               # missing.append(char)
       # if len(missing) > 0:
            #string = 'missing '
           # for letter in missing:
                #string = string + letter



    # Replace [] with the list of missing characters
    #return []







#if __name__ == "__main__":
    #ntests = int(sys.stdin.readline())

    #for i in range(ntests):
        #phrase = sys.stdin.readline().strip()
       # missing = solve(phrase)

        #if len(missing) == 0:
           # print("pangram")
       # else:
            #print("missing", "".join(missing))
