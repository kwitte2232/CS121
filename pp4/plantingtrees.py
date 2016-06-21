import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/plantingtrees
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes a single parameter: a list of integers, each of
# which represents t_i (as described in the problem statement)

class Tree(object):
    def __init__(self, days, planted):
        self._days = days
        self._planted = planted
        self._matured = self.matured_day()
        self._length = self.length()

    @property
    def days(self):
        return self._days

    @property
    def planted(self):
        return self._planted

    @property
    def matured(self):
        return self._matured

    def matured_day(self):
        return self._days + self._planted

    @property
    def length(self):
        return self._length = len(self)

    def __repr__(self):
        return ('Maturation time ').join(self._days)

def solve(times):
    
    trees = []
    times.sort()
    times.reverse()
    for i, time in enumerate(times):
        curr_day = i + 1
        tree = Tree(time, curr_day)
        trees.append(tree)

    matured = []
    for t in trees:
        matured.append(t.matured)

    last_day = max(matured)

    party_day = last_day + 1

    # Replace 0 with the earliest day the party can be
    # organized (as described in the problem statement)
    return party_day


#if __name__ == "__main__":
    #tokens = sys.stdin.read().strip().split()

   # n = int(tokens.pop(0))

    #times = [int(t) for t in tokens]
    #assert len(times) == n

    #print(solve(times))
