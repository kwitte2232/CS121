import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/engineeringenglish
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes a single parameter: a list of strings, each corresponding
# to a line of input. You must return a list of strings where the strings
# have been converted as described in the problem statement.

class Word(object):
    def __init__(self, word):
        self._word = word
        self._lower = self.convert_to_lowercase(word)

    @property
    def word(self):
        return self._word

    @property
    def lower(self):
        return self._lower

    def convert_to_lowercase(self, word):
        return word.lower()

def solve(lines):
    
    #appearance = {"Word in file": []}
    appearance = []
    engineered = []
    for line in lines:
        string = ""
        current_line = line.split(" ")
        for w in current_line:
            curr_word = Word(w)
            if curr_word.lower not in appearance:
                appearance.append(curr_word.lower)
                string = string + curr_word.word + " "
            else: 
                string = string + ". "
        string = string + "\n"
        engineered.append(string)

    for row in engineered:
        print(row)

    return engineered


#if __name__ == "__main__":
    #lines = [s.strip() for s in sys.stdin.readlines()]

    #print("\n".join(solve(lines)))
